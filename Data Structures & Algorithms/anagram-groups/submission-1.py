class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()

        for s in strs:
            chars = [0]*26 # [0,0,...,0]
            for i in range(len(s)):
                chars[ord(s[i]) - ord('a')] += 1
            
            chars = [str(c) for c in chars]
            chars = " ".join(chars)

            if chars not in dic:
                dic[chars] = [s]
            else:
                dic[chars].append(s)
            
        return list(dic.values())
        
        