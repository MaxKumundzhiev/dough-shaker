"""
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

Given a string, find the length of the longest substring in it with at most two distinct characters.
"""


def foo(string: str) -> int:
    boundary = 2
    window_start = 0
    substring = {}
    max_length = 0

    for window_end in range(len(string)):
        end_char = string[window_end]
        substring[end_char] = substring.get(end_char, 0) + 1

        while len(substring) > boundary:
            start_char = string[window_start]
            substring[start_char] -= 1
            
            if substring[start_char] == 0:
                del substring[start_char]

            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length
        

