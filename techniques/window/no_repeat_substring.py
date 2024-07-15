"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring, which has no repeating characters.
"""

def non_repeat_substring(string: str):
    window_start = 0
    max_length = 0
    char_index_map = {}

    # Iterate through the string
    for window_end in range(len(string)):
        end_char = string[window_end]

        # If the character already exists in the map, update window start
        if end_char in char_index_map:
        # Ensure window_start doesn't move beyond the last occurrence of the character
            window_start = max(window_start, char_index_map[end_char] + 1)

        # Update character index in the map
        char_index_map[end_char] = window_end

        # Track the maximum length after each window adjustment
        max_length = max(max_length, window_end - window_start + 1)

    return max_length

non_repeat_substring("abcabcbb")