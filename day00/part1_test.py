from .part1 import compute

import pytest

INPUT_S = """\

"""
EXPECTED = 0


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected
