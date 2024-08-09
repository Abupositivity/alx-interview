#!/usr/bin/python3
""" Minimum Operation's Module"""


def minOperations(n):
    """
    Gets the fewest no of ops needed to end up with exactly
    n 'x' characters.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n /= factor
        factor += 1

    return operations
