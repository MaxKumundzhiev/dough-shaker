"""
https://leetcode.com/problems/valid-palindrome/

- check if input is empty --> False
- preprocess phrase
    - split() -> list[A, man, a, plan, a, cancal, Panama] O(n)
    - merge words into single string -- "".join(iterable) O(n)
    - lowercase**
- use 2 pointers, from start and end

Time O(3n)  --> O(n)
Space O(2n) --> O(n)
"""

class Solution:
    def remove_auxiliary_characters(self, text):
        import string

        auxiliary_chars = string.punctuation + string.whitespace
        cleaned_text = ''.join([char for char in text if char not in auxiliary_chars])
        return cleaned_text
    
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return False

        words = s.split()
        if bool(words) is False:
            return True
        
        entity = "".join(words)
        cleansed = self.remove_auxiliary_characters(text=entity)

        l, r = 0, len(cleansed)-1
        while l <= r:
            lChar, rChar = cleansed[l].lower(), cleansed[r].lower()
            if lChar != rChar:
                return False
            else:
                l += 1
                r -= 1
        return True
        