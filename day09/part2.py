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


def shift(arr: list[str]) -> list[str]:
    n = len(arr)

    # Collect groups of digits from right to left
    groups = []
    i = n - 1
    while i >= 0:
        if arr[i].isdigit():
            group_end = i
            while i >= 0 and arr[i] == arr[group_end]:
                i -= 1
            group_start = i + 1
            # Record start and end indices of the group
            groups.append((group_start, group_end))
        else:
            i -= 1

    for file_start, file_end in groups:
        file_size = file_end - file_start + 1

        left = 0
        while left < file_start:
            if arr[left:left + file_size] == ['.'] * file_size:
                # Move left group
                arr[left:left + file_size] = arr[file_start:file_end+1]
                arr[file_start:file_end+1] = ['.'] * file_size

                break

            left += 1

    return arr


def compute(s: str) -> int:
    data = parse_to_format(s)

    data = shift(data)

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
EXPECTED = 2858


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected
