#!/usr/bin/python3
"""UTF-8 Validation"""


def check_next_valid(arr, width, span):
    """Checks if the next value is valid"""
    if width >= span and not all(list(map(
        lambda x: x & 0xC0 == 0x80,
        [next(arr) for _ in range(span-1)],
    ))):
        return False
    return True


def validUTF8(data):
    """
    Check that a sequence of byte values follows the UTF-8 encoding
    rules.  Does not check for canonicalization
    (i.e. overlong encodings
    are acceptable).
    """
    if not isinstance(data, list):
        return False
    size = len(data)
    if size == 0:
        return True
    data = iter(data)
    for idx, n in enumerate(data):
        if type(n) != int or n < 0 or n > 0x10ffff:
            return False

        elif n < 0x7F:
            continue

        elif n & 0xE0 == 0xC0:
            # 2-byte utf-8 character encoding
            span = 2

        elif n & 0xF0 == 0xE0:
            # 3-byte utf-8 character encoding
            span = 3

        elif n & 0xF8 == 0xF0:
            # 4-byte utf-8 character encoding
            span = 4

        else:
            return False

        if not check_next_valid(data, size-idx, span):
            return False
    return True
