#!/usr/bin/python3
"""Prime Game
Maria and Ben are playing a game. Given a set of consecutive integers starting
1 up to and including n, they take turns choosing a prime number the
set and removing that number and its multiples the set. The player that
cannot make a move loses the game.
"""


def isWinner(x, nums):
    """Prime Game"""
    if not nums or x < 1:
        return None
    n, c, p1 = max(nums), 0, 0
    aux = [True] * len(range(max(n + 1, 2)))
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not aux[i]:
            continue
        for j in range(i*i, n + 1, i):
            aux[j] = False

    aux[0] = aux[1] = False
    for i in range(len(aux)):
        if aux[i]:
            c += 1
        aux[i] = c

    for n in nums:
        p1 += aux[n] % 2 == 1

    if p1 * 2 == len(nums):
        return None

    if p1 * 2 > len(nums):
        return "Maria"
    return "Ben"
