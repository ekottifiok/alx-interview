#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Check that a sequence of byte values follows the UTF-8 encoding
    rules.  Does not check for canonicalization
    (i.e. overlong encodings
    are acceptable).
    """
    if not data or not isinstance(data, list):
        return False

    for n in data:
        if not isinstance(n, int) or n > 0x7f or n < 0:
            return False

    return True
