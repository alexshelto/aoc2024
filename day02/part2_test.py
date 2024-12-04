from .part2 import compute, check_level

import support
import pytest

INPUT_S = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
EXPECTED = 4


@pytest.mark.parametrize(('input_s', 'expected'), ((INPUT_S, EXPECTED),))
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
        ('31 37 38 41 44 46', True),
    ),
)
def test_check_level(input_s: str, expected: bool) -> None:
    assert check_level(support.parse_numbers_split(input_s)) == expected
