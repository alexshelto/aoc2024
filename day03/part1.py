from __future__ import annotations

import argparse
import os.path
import pytest
import re

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"


def compute(s: str) -> int:
    total = 0
    matches = re.findall(pattern, s)
    for tup in matches:
        total += int(tup[0]) * int(tup[1])
    return total


INPUT_S = """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
EXPECTED = 161


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", nargs="?", default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
