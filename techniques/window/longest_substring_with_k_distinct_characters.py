"""
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

Given a string, find the length of the longest substring in it with no more than K distinct characters.
You can assume that K is less than or equal to the length of the given string.



Notes:
    - construct valid substring (construct until substring become invalid through hash map)
    - manage invalid substring to make it valid (find such a char (window_start) when hash map will be valid (unique chars))

input = ....
longest_substring  <--> K (unique chars in substring)

we will get such a string that amount chars in string >= amount of unique chars in string --> garant that we will have such a substring



abc     k=1 --> longest 1
aaa     k=1 --> longest 3
aaabc   k=1 --> longest 3
 

aaabcaaaa
|   |
s   e

a: 2
b: 1


1. construct longest substring (window) until amount unique chars <= K
    - hashmap for stroing amount unique chars

    
n. compare longest substring (window)

"""

def longest_substring_with_k_distinct(string: str, k: int) -> int:
    window_start = 0
    max_length = 0
    char_frequency = {}

    # Iterate through the string
    for window_end in range(len(string)):
        end_char = string[window_end]
        char_frequency[end_char] = char_frequency.get(end_char, 0) + 1  # Initialize or increment count

        # Shrink window while exceeding the maximum distinct characters
        while len(char_frequency) > k:
            start_char = string[window_start]
            char_frequency[start_char] -= 1

            # Remove character from frequency map if count becomes zero
            if char_frequency[start_char] == 0:
                del char_frequency[start_char]

            window_start += 1

        # Update maximum length after each window adjustment
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


assert(longest_substring_with_k_distinct("aaabacaaaa", 2) == 6)