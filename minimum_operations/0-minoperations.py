#!/usr/bin/python3

def minOperations(n):
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
