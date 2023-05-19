#!/usr/bin/python3
"""Change comes from within module
"""


def makeChange(coins, total):
    """Given a pile of coins of different values, determine
    the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list[int]): coins is a list of the values of the
            coins in your possession
        total (int): the total hoped to acheive

    Returns:
        _type_: _description_
    """
    if total < 1:
        return 0
    count = 0

    for item in sorted(coins, reverse=True):
        while total - item >= 0:
            total -= item
            count += 1

    return count if total == 0 else -1
