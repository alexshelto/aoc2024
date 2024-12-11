from __future__ import annotations

import argparse
import pytest
import os.path

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


'''
KEEPING THIS SOLUTION FOR PART 1, THE LIMITATIONS OF LISTS ARE REACHED
AND IT WONT WORK FOR PART 2
'''


def compute(s: str) -> int:
    arr = s.strip().split(' ')

    iterations = 25

    for i in range(iterations):

        new_arr = []

        for idx, val in enumerate(arr):
            if val == '0':
                new_arr.append('1')
            elif len(val) % 2 == 0:
                mid = len(val) // 2
                first_half = int(val[:mid])
                last_half = int(val[mid:])
                new_arr.append(str(first_half))
                new_arr.append(str(last_half))
            else:
                new_arr.append(str(int(val) * 2024))

        arr = new_arr

    return len(arr)


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
125 17
"""
EXPECTED = 55312


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected
