"""
https://leetcode.com/problems/missing-number/

Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
"""

from typing import List


def missingNumber(nums: List[int]) -> int:
    max_, occurrences = max(nums), {}

    for number in range(max_+2):
        occurrences[number] = False
    
    for number in nums:
        occurrences[number] = True
    
    for key, value in occurrences.items():
        if value is False:
            return key
    
    return None


def foo(nums: List[int]) -> int:
    ...