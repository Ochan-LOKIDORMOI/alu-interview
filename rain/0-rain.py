#!/usr/bin/python3
"""
Module to calculate amount of water retained after rain on walls.

rain(walls)
  - Calculate total amount of water retained given heights of walls
  - walls is a list of non-negative integers representing wall heights
  - Returns an integer
  """


def rain(walls):
    """
  Calculate total amount of water retained.  

  Args:
    walls (list): List of non-negative integers representing wall heights

  Returns:
    int: Total amount of water retained
  """
    if not walls or len(walls) < 3:
        return 0

    water = 0
    for i in range(1, len(walls) - 1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])
        right = walls[i]
        for j in range(i + 1, len(walls)):
            right = max(right, walls[j])
        water += min(left, right) - walls[i]

    return water
