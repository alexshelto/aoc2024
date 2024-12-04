from __future__ import annotations

import argparse
import pytest
import os.path

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")

TARGET = "MAS"


def compute(s: str) -> int:
    count = 0
    coords = support.parse_coords_str(s)

    x_locs = [key for key, value in coords.items() if value == "X"]

    for point in x_locs:
        count += is_xmas(point, coords)
    return count


def is_xmas(p: tuple[int, int], coords: dict[tuple[int, int], str]) -> int:
    count = 0

    # Take the next 3 points in each direction:
    for offset in support.XY_8Offsets:
        next_3_pts = support.GridNav.next_n_points(offset, p, 3)

        built_word = [coords.get(point, ".") for point in next_3_pts]

        if built_word == ["M", "A", "S"]:
            count += 1

    return count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", nargs="?", default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


###############
#   TESTING   #
###############
INPUT_S = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
EXPECTED = 18


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected
