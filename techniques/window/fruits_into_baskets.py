"""
https://leetcode.com/problems/fruit-into-baskets/

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.



input = [1, 2, 1, 0, 2, 2]
         |
                  |
"""

def foo(nums: List[int]):
    buckets = 2
    window_start = 0
    max_len = 0
    hash_map = {}
    
    for window_end in range(len(nums)):
        end_tree = nums[window_end]
        hash_map[end_tree] = hash_map.get(end_tree, 0) + 1
    
        while len(hash_map) > buckets:
            start_tree = nums[window_start]
            hash_map[start_tree] -= 1

            if hash_map[start_tree] == 0:
                del hash_map[start_tree]

            window_start += 1

        max_len = max(max_len, window_end - window_start + 1)
    
    return max_len