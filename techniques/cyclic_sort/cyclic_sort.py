"""
We are given an array containing n objects. Each object, when created, was assigned a unique number from 1 to n based on their creation sequence.
This means that the object with sequence number 3 was created just before the object with sequence number 4.

Write a function to sort the objects in-place on their creation sequence number in O(n) and without any extra space.


input --> [2, 3, 4, 1]
output --> [1, 2, 3, 4]  # inplace


Idea:
    - for each element we need to find its correct place (idx)
    - while the element is not on it's correct place, swap currnet element with element sitting on current element's idx obtained from value  
"""

from typing import List


def foo(array: List[int]) -> List[int]:
    idx, iteration = 0, len(array) - 1

    while idx < iteration:
        expected = array[idx] - 1
        
        if idx == expected:
            idx += 1
        
        else:
            while idx != expected:
                array[idx], array[expected] = array[expected], array[idx]
                expected = array[idx] - 1
            idx += 1
    return array



sorted_list = foo([3, 1, 5, 4, 2])
print(sorted_list)  # Output: [1, 2, 3, 4, 5]