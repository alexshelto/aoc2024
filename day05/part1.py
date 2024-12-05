from __future__ import annotations

import argparse
import pytest
import os.path

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def build_after_dict(s: str) -> dict[int, set[int]]:
    seen_after: dict[int, set[int]] = {}
    for line in s.splitlines():
        before, after = line.split('|')
        if int(after) not in seen_after:
            seen_after[int(after)] = set()
        seen_after[int(after)].add(int(before))

    return seen_after


def is_valid_line(ar: list[int], d: dict[int, set[int]]) -> bool:
    for x in range(len(ar)):
        for y in range(x + 1, len(ar)):
            ptr = ar[y]
            before = ar[x]
            cant_be_in: set[int] = d.get(ptr, set())
            if before in cant_be_in:
                return False
    return True


def compute(s: str) -> int:
    total = 0

    rules, page_nums = s.split('\n\n')
    mappings = build_after_dict(rules)

    for line in page_nums.splitlines():
        nums = [int(x) for x in line.split(',')][::-1]
        if is_valid_line(nums, mappings):
            total += nums[len(nums)//2]

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
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
EXPECTED = 143


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected
