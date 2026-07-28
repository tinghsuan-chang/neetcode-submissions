class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        chars = []

        for i in range(len(s)):
            if s[i].isalnum():
                chars.append(s[i])
        
        l = 0
        r = len(chars) - 1
        while l < r:
            if chars[l] != chars[r]:
                return False
            else:
                l += 1
                r -= 1
        
        return True