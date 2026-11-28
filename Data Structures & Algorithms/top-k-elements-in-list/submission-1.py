from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = defaultdict(int) # {1:1, 2:2, 3:3}
        for num in nums:
            num_freq[num] += 1
        
        freqs = [[] for _ in range(len(nums))] 
        for num, freq in num_freq.items():
            freqs[freq - 1].append(num)
        
        res = []
        i = -1
        while len(res) < k:
            if freqs[i]:
                for num in freqs[i]:
                    res.append(num)
            i -= 1
        
        return res


        

            