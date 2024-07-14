"""
https://leetcode.com/problems/largest-subarray-length-k/

Given an array of positive numbers and a positive number K,
find the maximum sum of any contiguous subarray of size K.

Array: [1, 3, 2, 6, 1, 4, 1, 8, 2], K=5
           |
                       |
"""

from typing import List

# Time O(n) | Space O(1)
def foo(array: List[int], k: int) -> int:
    maximum_sum = None
    window_start = 0
    window_sum = None

    for window_end in range(len(array)):
        if window_sum is None:
            window_sum = array[window_end]
        else:
            window_sum += array[window_end]
        
        if window_end >= k - 1:
            if maximum_sum is None:
                maximum_sum = window_sum
            else:
                maximum_sum = max(maximum_sum, window_sum)
                window_sum -= array[window_start]
                window_start += 1
    return maximum_sum

