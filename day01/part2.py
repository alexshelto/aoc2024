from __future__ import annotations

import argparse
from collections import Counter
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

    right_counts = Counter(right)

    for num in left:
        sim_score = num * right_counts[num]
        ret += sim_score

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
