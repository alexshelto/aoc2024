from __future__ import annotations

import argparse
import pytest
import os.path

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def trail_score(grid: dict[tuple[int, int], int], pt: tuple[int, int]) -> int:
    queue = [pt]
    ends = []

    while queue:
        ptr = queue.pop()
        cur = grid[ptr]
        next_val = cur + 1

        for next_pt in support.adjacent_4(ptr[0], ptr[1]):
            if next_pt in grid and grid[next_pt] == next_val:
                if next_val == 9:
                    ends.append(next_pt)
                else:
                    queue.append(next_pt)

    return len(ends)


def compute(s: str) -> int:
    grid = support.parse_coords_int(s)
    trail_heads = [point for point, value in grid.items() if value == 0]

    total = 0

    for th in trail_heads:
        found = trail_score(grid, th)
        total += found

    return total


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
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""
EXPECTED = 81


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected
