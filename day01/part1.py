from __future__ import annotations

import argparse
import os.path

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    ret = 0
    left = []
    right = []

    lines = s.splitlines()
    for line in lines:
        numbers = support.parse_numbers_split(line)
        left.append(numbers[0])
        right.append(numbers[1])

    assert len(right) == len(left)
    left.sort()
    right.sort()

    while len(left) > 0 and len(right) > 0:
        v1 = left.pop()
        v2 = right.pop()
        ret += abs(v1-v2)

    return ret


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
