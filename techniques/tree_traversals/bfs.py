class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return False

        words = s.split()
        if bool(words) is False:
            return False
        
        entity = "".join(words)

        l, r = 0, len(entity)-1
        while l <= r:
            lChar, rChar = entity[l].lower(), entity[r].lower()
            if lChar != rChar:
                return False
            else:
                l += 1
                r -= 1
        return True
        
print(Solution().isPalindrome(s=" "))