from __future__ import annotations

import argparse
import pytest
import os.path

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def can_math(target: int, nums: list[int]) -> bool:
    possibles = [nums.pop(0)]
    while nums:
        cur = nums.pop(0)
        temp = []
        for p in possibles:
            next = [
                p + cur,
                p * cur,
            ]
            temp.extend([v for v in next if v <= target])
        possibles = temp

    return target in possibles


def compute(s: str) -> int:
    total = 0
    for line in s.splitlines():
        splits = line.split(':')
        digits = [int(num) for num in splits[1].strip().split(' ')]

        target = int(splits[0])

        if can_math(target, digits):
            total += target

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
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
EXPECTED = 3749


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected
