from __future__ import annotations

import argparse
import os.path
import pytest
import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    ret = 0
    lines = s.splitlines()
    for line in lines:
        report = support.parse_numbers_split(line)
        if is_safe(report):
            ret += 1
    return ret

MAX_DIFFERENCE = 3

def is_safe(l: list[int]) -> bool: 
    differs = [a - b for a, b in zip(l, l[1:])]

    isMonotonic = all(i > 0 for i in differs) or all(i < 0 for i in differs)
    inRange = all(abs(i) <= MAX_DIFFERENCE for i in differs)

    return isMonotonic and inRange


INPUT_S = '''\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''
EXPECTED = 2


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
