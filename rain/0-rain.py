#!/usr/bin/python3

"""
Module to calculate amount of water retained after rain on walls.

This module contains one function:

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

  if not walls:
    return 0

  total_water = 0
  left = 0
  right = len(walls) - 1
  left_max = walls[left]
  right_max = walls[right]

  while left < right:

    # calculate trapped water on smaller side

    return total_water
