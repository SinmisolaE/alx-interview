#!/usr/bin/python3

""" def isWinner(x, nums)
  where x is the number of rounds and nums is an array of n
"""


def isWinner(x, nums):
    """ Return: name of the player that won the most rounds
        If the winner cannot be determined, return None
        You can assume n and x will not be larger than 10000
        You cannot import any packages in this task
    """

    if (x < 1) or (not nums):
        return None

    n_max = max(nums)

    is_prime = [True] * (n_max + 1)

    is_prime[0], is_prime[1] = False, False

    for p in range(2, int(n_max ** 0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n_max + 1, p):
                is_prime[i] = False

    prime_counts = [0] * (n_max + 1)
    for i in range(1, n_max + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if is_prime[i] else 0)

    marie, ben = 0, 0
    for n in nums:
        if prime_counts[n] % 2 == 1:
            marie += 1
        elif prime_counts[n] % 2 == 0:
            ben += 1

    if marie > ben:
        return "Marie"
    elif ben > marie:
        return "Ben"
    else:
        return None
