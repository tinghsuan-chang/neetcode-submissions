class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        chars = set({s[0]})
        max_length = 1
        l, r = 0, 1
        while r < len(s):
            if s[r] in chars:
                while (l < r) and (s[r] in chars):
                    chars.remove(s[l])
                    l += 1
            chars.add(s[r])
            r += 1
            max_length = max(max_length, len(chars))
        
        return max_length


            
