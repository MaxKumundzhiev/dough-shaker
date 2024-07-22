"""
https://leetcode.com/problems/permutation-in-string/
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

- permutation - когда количество уникальных символов в строке равняется кол-ву уникальных символов в подстроке
- строка (s2) и паттерн (s1)
- нужно итерироваться по строке до тех пор пока не встретим ровно по одному разу символы из паттерна


Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

s1 = "ab", s2 = "eidboaoo"

hash_map = {}
for char in patter:
    remainin_characters_in_pattern += 1
    hash_map[char] = hash_map.get(char, 0) + 1

a: 1
b: 1

eidboaoo
   |

eidbaooo
|
   |

a: 4
b: 3
"""

def foo():
    # Create a character frequency dictionary for the pattern
    char_freq = {}
    for char in pattern:
        char_freq[char] = char_freq.get(char, 0) + 1

    # Use a sliding window approach
    window_start = 0
    matches = 0  # Track the number of characters in the window that match the pattern

    for window_end in range(len(string)):
        end_char = string[window_end]

        # Update character frequency for the current character in the window
        if end_char in char_freq:
            char_freq[end_char] -= 1
        
            if char_freq[end_char] == 0:
                matches += 1  # Increment matches if a character's frequency reaches 0

        # Check if the window matches the pattern (all characters with frequency 0)
        if matches == len(char_freq):
            return True

        # Shrink the window if necessary (after processing window_end)
        if window_end >= len(pattern) - 1:
            start_char = string[window_start]
            window_start += 1

        if start_char in char_freq:
            if char_freq[start_char] == 0:
                matches -= 1  # Decrement matches if removing a character breaks the pattern
                char_freq[start_char] += 1

    return False