from __future__ import annotations

import argparse
from collections import defaultdict
import pytest
import os.path

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def double_point(p: tuple[int, int]) -> tuple[int, int]:
    x, y = p
    return (x*2, y*2)


def add_points(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[int, int]:
    x1, y1 = p1
    x2, y2 = p2

    return (x1+x2, y1+y2)


def compute(s: str) -> int:
    grid = support.parse_coords_str(s)

    antennas = defaultdict(list)
    for y_idx, line in enumerate(s.splitlines()):
        for x_idx, val in enumerate(line):
            if val == '.':
                continue
            antennas[val].append((x_idx, y_idx))

    antinodes = set()

    for antenna, coords in antennas.items():
        for first in antennas[antenna]:
            for second in antennas[antenna]:
                if first == second:
                    continue
                slope = (second[0]-first[0], second[1] - first[1])

                relative = double_point(slope)
                abs_anti = add_points(first, relative)

                if abs_anti in grid:
                    antinodes.add(abs_anti)

    return len(antinodes)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())


###############
#   TESTING   #
###############

INPUT_S = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
EXPECTED = 14


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected
