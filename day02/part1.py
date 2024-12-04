from __future__ import annotations

import argparse
import os.path
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


def is_safe(ar: list[int]) -> bool:
    differs = [a - b for a, b in zip(ar, ar[1:])]

    isMonotonic = all(i > 0 for i in differs) or all(i < 0 for i in differs)
    inRange = all(abs(i) <= MAX_DIFFERENCE for i in differs)

    return isMonotonic and inRange


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
