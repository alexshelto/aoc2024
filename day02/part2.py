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
        print(report)
        if check_level(report):
            ret += 1
    return ret

def check_level(l: list[int]) -> bool: 
    if is_safe(l, None): 
        return True

    for i in range(0, len(l)): 
        if is_safe(l, i): 
            return True

    return False

def is_safe(l: list[int], skip_index: int | None) -> bool: 
    new_list = l.copy()
    if skip_index is not None: 
        new_list = l[:skip_index] + l[skip_index + 1:]

    differs = [a - b for a, b in zip(new_list, new_list[1:])]

    isMonotonic = all(i > 0 for i in differs) or all(i < 0 for i in differs)
    inRange = all(abs(i) <= 3 for i in differs)

    return isMonotonic and isInRange


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0

if __name__ == '__main__':
    raise SystemExit(main())


INPUT_S = '''\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''
EXPECTED = 4

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    )
)
def test_is_safe(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('9 2 3 4 5', True),
        ('1 9 3 4 5', True),
        ('1 2 9 4 5', True),
        ('1 2 3 9 5', True),
        ('1 2 3 4 9', True),
        ('1 2 3 4 5 5', True),
        ('1 2 7 8 9', False),
        ('29 28 27 25 26 25 22 20', True),
        ('31 37 38 41 44 46', True)
    ),
)
def test_check_level(input_s: str, expected: bool) -> None: 
    assert check_level(support.parse_numbers_split(input_s)) == expected

