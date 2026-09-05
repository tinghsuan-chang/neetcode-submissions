class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        chars = {s[0]}
        max_length = 1
        l, r = 0, 1
        for r in range(1, len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            max_length = max(max_length, len(chars))
        
        return max_length

# Time: O(n)
# Space: O(m), m: number of unique characters
            
