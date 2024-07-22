"""
https://leetcode.com/problems/maximum-average-subarray-i/

Given an array, find the average of all contiguous subarrays of size K in it.
Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
"""

"""
Naive approach

Traverse from left to right the array with window of size K and count the average.
 [1, 3, 2, 6, -1, 4, 1, 8, 2]
  |  |  |  |   |  |  |  |  |
  1  2  3  4   1  2  3  4  5
               5


Time complexity: 
    Since for every element of the input array, 
    we are calculating the sum of its next K elements, 
    the time complexity of the above algorithm will be O(N*K) 
    where N is the number of elements in the input array.

def foo(array: List[int], k: int) -> int:
    averages = []
    elements = len(array)
    left, right = 0, elements // k

    while right <= elements-1:
        average = sum(array[left:right]) // k
        averages.append(average)
    
    return sum(averages) // k
"""

"""
Optimized approach

We will slide the window by one element when we move on to the next subarray. 
To reuse the sum from the previous subarray, we will subtract the element going out 
of the window and add the element now being included in the sliding window.

[1, 3, 2, 6, -1, 4, 1, 8, 2]

window_sum = 11 - 1 = 10

def foo(array: List[int], k: int) -> int:
    results = []
    window_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        # Add the next element to the window sum
        window_sum += arr[window_end]

        # Check if we have reached the window size
        if window_end >= k - 1:
            # Calculate and append the average of the current window
            results.append(window_sum / k)

            # Slide the window forward by removing the element going out
            window_sum -= arr[window_start]

            # Increment window start for the next iteration
            window_start += 1

    return results
"""

from typing import List


def foo(array: List[int], k: int) -> int:
    results = []
    window_sum = 0
    window_start = 0

    for window_end in range(len(array)):
        # Add the next element to the window sum
        window_sum += array[window_end]

        # Check if we have reached the window size
        if window_end >= k - 1:
            # Calculate and append the average of the current window
            results.append(window_sum / k)

            # Slide the window forward by removing the element going out
            window_sum -= array[window_start]

            # Increment window start for the next iteration
            window_start += 1

    return results

foo(array=[1, 3, 2, 6, -1, 4, 1, 8, 2], k=5)


## leetcode
def findMaxAverage(self, nums: List[int], k: int) -> float:        
        average = None
        left, sum_ = 0, None

        for right in range(len(nums)):
            if sum_ is None:
                sum_ = nums[right]
            else:
                sum_ += nums[right]

            if right >= k - 1:
                current = sum_ / k
                if average is None:
                    average = current
                else:
                    average = max(current, average)
                sum_ -= nums[left]
                left += 1


def foo(array: List[int], size:int) -> int:
    window_start, max_, window_sum_ = 0, float("-inf"), 0
    
    for window_end in range(len(array)):
        if window_end > size - 1:
            window_sum_ -= array[window_start]
            window_start += 1
    
        window_sum_ += array[window_end]
        max_ = max(max_, window_sum_)
    return max_

assert foo(array=[1, 2, 3, 4], size=3) == 9