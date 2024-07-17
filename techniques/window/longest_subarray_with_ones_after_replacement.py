"""
https://leetcode.com/problems/max-consecutive-ones-iii/
> Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.


Given an array containing 0's and 1's, if you are allowed to replace no more than K 0's with 1's, 
find the length of the longest contiguous subarray having all 1's.


[1,1,1,0,0,0,1,1,1,1,0], k = 2
- массив 0 и 1
- нужно найти интервал чтобы в нем последовательно было большее кол-во 1 после K замен
- нужно строить интервал пока нулей в нем будет < K
"""

from typing import List


def longestOnes(nums: List[int], k: int) -> int:
    window_start = 0
    flips = 0
    max_len = 0
    
    for window_end in range(len(nums)):
        if nums[window_end] == 0:
            flips += 1

        while flips > k:
            if nums[window_start] == 0:
                flips -= 1
            window_start += 1

        max_len = max(max_len, window_end - window_start + 1)
    
    return max_len


