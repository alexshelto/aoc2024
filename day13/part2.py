from __future__ import annotations

import argparse
import pytest
import os.path
import re

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

add = 10000000000000


def compute(s: str) -> int:
    ans = 0

    for group in s.split('\n\n'):
        a_x, a_y, b_x, b_y, p_x, p_y = map(int, re.findall(r'\d+', group))

        p_x += add
        p_y += add

        c_a = ((p_x * b_y) - (p_y * b_x)) / ((a_x * b_y) - (a_y * b_x))
        c_b = (p_x - a_x * c_a) / b_x

        if c_a % 1 == c_b % 1 == 0:
            ans += int(c_a * 3 + c_b)

    return ans


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
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""
EXPECTED = 480


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected
