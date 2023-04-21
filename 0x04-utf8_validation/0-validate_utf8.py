#!/usr/bin/python3
"""UTF-8 Validation"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Check that a sequence of byte values follows the UTF-8 encoding
    rules.  Does not check for canonicalization
    (i.e. overlong encodings
    are acceptable).
    """
    if not data or not isinstance(data, List):
        return False

    for n in data:
        if not isinstance(n, int) or len(f'{n:0>{7}b}') != 7:
            return False

    return True
