from __future__ import annotations

import argparse
import pytest
import os.path

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def parse_to_format(s: str) -> list[str]:
    data = []
    id = 0
    length = True
    for n in s.strip():
        if length:
            data.extend([str(id) for x in range(int(n))])
            id += 1
        else:
            data.extend(['.' for x in range(int(n))])

        length = not length
    return data


def compute(s: str) -> int:
    data = parse_to_format(s)

    print(''.join(data))

    left, right = 0, len(data)-1

    while left < len(data) and right > 0 and left < right:
        if data[left] == '.' and data[right] != '.':
            data[left], data[right] = data[right], data[left]
            left += 1
            right -= 1
        elif data[left] != '.':
            left += 1
        elif data[right] == '.':
            right -= 1

    total = 0
    for idx, val in enumerate(data):
        if val == '.':
            continue
        total += idx * int(val)

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
2333133121414131402
"""
EXPECTED = 1928


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected
