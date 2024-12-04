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
        print(report)
        if check_level(report):
            ret += 1
    return ret


def check_level(ar: list[int]) -> bool:
    if is_safe(ar, None):
        return True

    for i in range(0, len(ar)):
        if is_safe(ar, i):
            return True

    return False


def is_safe(ar: list[int], skip_index: int | None) -> bool:
    new_list = ar.copy()
    if skip_index is not None:
        new_list = ar[:skip_index] + ar[skip_index + 1:]

    differs = [a - b for a, b in zip(new_list, new_list[1:])]

    isMonotonic = all(i > 0 for i in differs) or all(i < 0 for i in differs)
    inRange = all(abs(i) <= 3 for i in differs)

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
