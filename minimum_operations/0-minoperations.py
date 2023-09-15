#!/usr/bin/python3
"""
Minimum operations
"""
def minOperations(n):
    """
    Returns the operations
    """
     a = 0
    b = 2
    while n > 1:
        while n % b == 0:
            a += b
            n = n / b
        b += 1
    return a
