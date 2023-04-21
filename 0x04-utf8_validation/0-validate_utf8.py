#!/usr/bin/python3
"""UTF-8 Validation"""
from typing import List

LENONEBYTE = 7


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
        if len(f'{n:0>{LENONEBYTE}b}') != LENONEBYTE:
            return False

    return True
