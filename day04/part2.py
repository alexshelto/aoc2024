from __future__ import annotations

import argparse
import pytest
import os.path

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    count = 0
    coords = support.parse_coords_str(s)

    a_locs = [key for key, value in coords.items() if value == "A"]

    for point in a_locs:
        if can_spell_xmas_from_point(point, coords):
            count += 1

    return count


DIRECTIONS = [
    [support.XY_8Offsets.UP_LEFT, support.XY_8Offsets.DOWN_RIGHT],
    [support.XY_8Offsets.UP_RIGHT, support.XY_8Offsets.DOWN_LEFT],
]


def can_spell_xmas_from_point(
    p: tuple[int, int], coords: dict[tuple[int, int], str]
) -> bool:

    # Use offsets and get diagonal points
    for offset in DIRECTIONS:
        p1 = support.GridNav.next_n_points(offset[0], p, 1)[
            0]  # index 0 only 1 point
        p2 = support.GridNav.next_n_points(offset[1], p, 1)[0]

        letters = {coords.get(p1, "."), coords.get(p2, ".")}

        if letters != {"M", "S"}:
            return False

    return True


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
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
"""
EXPECTED = 9


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected
