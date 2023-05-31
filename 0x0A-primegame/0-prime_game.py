#!/usr/bin/python3
"""Prime Game Module
"""


def isWinner(x, nums):
    """the main function isWinner to compute

    Args:
        x (int): _description_
        nums (list[int]): _description_

    Returns:
        Ben or Maria: _description_
    """
    if x < 1 or not nums:
        return None
    max_n = max(nums)
    primes = []

    def calculate_primes():
        """We can precalculate the primes up to the maximum 'n'
        that can occur in any round. This will help us
        optimize the prime number selection during gameplay.

        Args:
            n (int): _description_

        Returns:
            list[int]: _description_
        """

        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(max_n**.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_n + 1, i):
                    is_prime[j] = False

        for i in range(2, max_n + 1):
            if is_prime[i]:
                primes.append(i)

    calculate_primes()
    winners = []

    for n in nums:
        is_maria_winner = True

        if n % 2 == 1:
            count_primes = sum(1 for p in primes if p <= n)
            if count_primes % 2 == 0:
                is_maria_winner = False

        winners.append("Maria" if is_maria_winner else "Ben")
    if winners.count('Maria') != winners.count('Ben'):
        return winners[-1]
