"""
https://leetcode.com/problems/longest-repeating-character-replacement/description/

Given a string with lowercase letters only, if you are allowed to replace no more than K letters with any letter, 
find the length of the longest substring having the same letters after replacement.

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.


Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.


Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.



AABABBA

AAAABBA
AABBBBA

AABABBA
  |
    |

A: 1
B: 2

Нужнр заменить буквы не более чем K раз так чтобы строка сожержала одинаковые буквы и была самой длинной  

value = hash.values()
while sum(value - max(value)) > K:
    ...
"""

"""
AABABBA
 |
    |
"""

def length_of_longest_substring(string, k):
    window_start = 0
    max_length = 0
    max_repeat_letter_count = 0
    char_frequency = {}

    # Iterate through the string
    for window_end in range(len(string)):
        end_char = string[window_end]
        char_frequency[end_char] = char_frequency.get(end_char, 0) + 1  # Concise way to handle new/existing characters
        max_repeat_letter_count = max(max_repeat_letter_count, char_frequency[end_char])

        # Shrink window if needed
        # window_end - window_start + 1 -- length of interval (общее количество букв)
        # max_repeat_letter_count       -- characters which we might delete (буквы которые повторяются)
        # (общее количество букв) - (буквы которые повторяются) == буквы которые не повторяются (которые можно удалить) 

        if window_end - window_start + 1 - max_repeat_letter_count > k:
            start_char = string[window_start]
            char_frequency[start_char] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length