class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                res.append(subset.copy())
                if subset:
                    subset.pop()
                return
                
            # option 1: include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # option 2: skip nums[i]
            backtrack(i + 1)

        backtrack(0)
        return res



        