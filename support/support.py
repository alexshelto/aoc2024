from __future__ import annotations

import contextlib
import sys
import time
import re


def parse_numbers_split(s: str) -> list[int]:
    return [int(x) for x in s.split()]


def parse_numbers_comma(s: str) -> list[int]:
    return [int(x) for x in s.strip().split(",")]


def adjacent_4(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    """returns the coordinates to the top, right, left and below the given point"""
    yield x, y + 1
    yield x + 1, y
    yield x, y - 1
    yield x - 1, y


def adjacent_8(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    """U=up, D=down, R=right, L=left, UR=top right diagonal... returns U,UR,R,DR,D,DL,L,UL"""
    for y_offset in (-1, 0, 1):
        for x_offset in (-1, 0, 1):
            if y_offset == x_offset == 0:
                continue
            yield x + x_offset, y + y_offset


def parse_coords_int(s: str) -> dict[tuple[int, int], int]:
    """parse numbers into coordinate system"""
    coords = {}
    y = 0
    for y_idx, line in enumerate(s.splitlines()):
        for x_idx, val in enumerate(line):
            coords[(x_idx, y_idx)] = int(val)
    return coords


@contextlib.contextmanager
def timing(name: str = "") -> Generator[None, None, None]:
    before = time.time()
    try:
        yield
    finally:
        after = time.time()
        t = (after - before) * 1000
        unit = "ms"
        if t < 100:
            t *= 1000
            unit = "μs"
        if name:
            name = f" ({name})"
        print(f"> {int(t)} {unit}{name}", file=sys.stderr, flush=True)
