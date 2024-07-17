"""
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
"""

from typing import List


def foo(array: List[int], target: int) -> List[int]:
    left, right = 0, len(array) - 1

    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == target:
            return [left, right]
        elif current_sum > target:
            right -= 1
        else:
            left += 1

    return -1


assert foo(array=[1, 2, 3, 4, 5], target=5) == [0, 3]
