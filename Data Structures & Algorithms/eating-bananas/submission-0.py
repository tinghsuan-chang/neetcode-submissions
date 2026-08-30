import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k, max_k = 1, max(piles) # lower, upper bound for k

        if h == len(piles):
            return max_k
        
        while min_k < max_k:
            k = (min_k + max_k) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / k)
            if time > h:
                min_k = k + 1
            else:
                max_k = k
        
        return max_k

        



        