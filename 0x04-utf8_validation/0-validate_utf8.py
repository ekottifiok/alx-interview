#!/usr/bin/python3
"""UTF-8 Validation"""
from typing import List


def count_leading_ones(byte: int) -> int:
    """counts leading ones

    Args:
        byte (int): _description_

    Returns:
        int: _description_
    """
    for i in range(8):
        if byte >> (7 - i) == 0b11111111 >> (7 - i) & ~1:
            return i
    return 8


def validUTF8(data: List[int]) -> bool:
    """
    Check that a sequence of byte values follows the UTF-8 encoding
    rules.  Does not check for canonicalization (i.e. overlong encodings
    are acceptable).

    """
    if not data or not isinstance(data, List):
        return False

    data = iter(data)   # type: ignore
    for leading_byte in data:
        leading_ones = count_leading_ones(leading_byte)
        if leading_ones in [1, 7, 8]:
            return False        # Illegal leading byte
        for _ in range(leading_ones - 1):
            trailing_byte = next(data, None)  # type: ignore
            if trailing_byte is None or trailing_byte >> 6 != 0b10:
                return False    # Missing or illegal trailing byte
    return True
