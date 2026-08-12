class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            digits = [int(d) for d in str(n)]
            sumsq = sum([d**2 for d in digits])
            if sumsq == 1:
                return True
            n = sumsq

        return False