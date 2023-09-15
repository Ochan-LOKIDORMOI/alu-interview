#!/usr/bin/python3

"""
Module to calculate the minimum number of operations (paste) needed to reach a target number of H characters in a file.

The file initially contains a single H character. Each paste operation doubles the current number of H's.

This module contains one function:

minOperations(n)
    - Calculates the minimum number of paste operations needed to reach a target of n H characters
    - Returns an integer
    - If the target n is not possible to reach, returns 0
"""


def minOperations(n):
    """
    Calculate minimum operations to reach target number of H characters.

    Args:
        n (int): Target number of H characters

    Returns:
        int: Minimum number of operations
        0 if target is not possible
    """

    if n < 1:
        return 0

    operations = 0
    current = 1

    while current < n:
        current *= 2
        operations += 1

    remainder = n - (2**operations - 1)
    if remainder == 0:
        return operations
    else:
        return 0
