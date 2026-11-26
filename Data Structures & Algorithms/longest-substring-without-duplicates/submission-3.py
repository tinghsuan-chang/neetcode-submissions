class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        l, r = 0, 1
        seen = {s[l]}
        res = 1

        while (l <= r) and (r < len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                seen.remove(s[l])
                l += 1
            res = max(res, len(seen))
        
        return res
        

                

