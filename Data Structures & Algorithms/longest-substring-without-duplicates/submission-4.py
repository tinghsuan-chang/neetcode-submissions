class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        seen = {s[0]}
        max_length = 1
        l = 0
        for r in range(1, len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            max_length = max(max_length, len(seen))
        
        return max_length

# Time: O(n), because each pointer advances at most n times
# Space: O(m), m: number of unique characters
            
