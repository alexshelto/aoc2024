from __future__ import annotations

from collections import defaultdict

import argparse
import pytest
import os.path

from typing import List

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def process_stone(val: str) -> List[str]:
    if val == '0':
        return ['1']
    elif len(val) % 2 == 0:
        mid = len(val) // 2
        first_half = str(int(val[:mid]))
        second_half = str(int(val[mid:]))
        return [first_half, second_half]
    else:
        return [str(int(val) * 2024)]


'''
CHANGED SOLUTION FROM PART1, LISTS WERE NO LONGER WORKING
STARTED THINKING ABOUT THE NUMBER OF DUPLICATES PER LIST, THERE
ENDS UP BEING THOUSANDS IF NOT TENS OF THOUSANDS, SO I USE DICTS
'''


def compute(s: str) -> int:
    iterations = 25

    stone_counts: dict[str, int] = defaultdict(int)
    for stone in s.strip().split(' '):
        stone_counts[stone] += 1

    for iter in range(iterations):
        new_counts: dict[str, int] = defaultdict(int)

        for stone, freq in stone_counts.items():

            resulting_stones = process_stone(stone)

            for new_stone in resulting_stones:
                new_counts[new_stone] += freq

        stone_counts = new_counts

    return sum(stone_counts.values())


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
125 17
"""
EXPECTED = 55312


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected
