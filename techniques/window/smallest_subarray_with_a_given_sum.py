"""
https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of positive numbers and a positive number S,
find the length of the smallest contiguous subarray whose sum is greater than or equal to S.

Return 0 if no such subarray exists.

array = 1, 2, 3, 4, 5, 6  | s = 4
        
"""

def smallest_subarray_with_given_sum(arr, s):
    window_sum = 0
    min_length = float('inf')
    window_start = 0
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        # Shrink the window while the sum is greater than or equal to the target
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)

            # Remove the first element from the window sum and advance the start pointer
            window_sum -= arr[window_start]
            window_start += 1

    # Return 0 if no subarray with the target sum exists
    return 0 if min_length == float('inf') else min_length


assert(smallest_subarray_with_given_sum(arr=[1, 2, 3, 4, 5, 6], s=4) == 1)