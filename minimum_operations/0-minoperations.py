#!/usr/bin/python3
"""
Minimum operations
"""
def minOperations(n):
    """
    Returns the operations
    """
    if n <= 1:
        return n

    operations = 0
    current_length = 1
    clipboard = 0

    while current_length < n:
        if n % current_length == 0:
            clipboard = current_length
        operations += 1
        current_length += clipboard

    return operations
