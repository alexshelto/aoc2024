from __future__ import annotations

import support


def test_parse_numbers_split() -> None:
    assert support.parse_numbers_split("1 2 3") == [1, 2, 3]
    assert support.parse_numbers_split("  1 \n2  \n 3") == [1, 2, 3]


def test_parse_numbers_comma() -> None:
    assert support.parse_numbers_comma("  1, 2,  3") == [1, 2, 3]
    assert support.parse_numbers_comma("  1, 2,  3\n") == [1, 2, 3]


def test_adjacent_4() -> None:
    pts = set(support.adjacent_4(5, 5))
    assert pts == {(5, 6), (6, 5), (5, 4), (4, 5)}


def test_adjacent_8() -> None:
    pts = set(support.adjacent_8(5, 5))
    assert pts == {(4, 6), (5, 6), (6, 6), (4, 5), (6, 5), (4, 4), (5, 4), (6, 4)}


def test_parse_coords_int() -> None:
    coords = support.parse_coords_int("123\n456")
    assert coords == {
        (0, 0): 1,
        (1, 0): 2,
        (2, 0): 3,
        (0, 1): 4,
        (1, 1): 5,
        (2, 1): 6,
    }
