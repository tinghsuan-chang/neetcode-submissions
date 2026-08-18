class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                res.append(subset.copy()) # Time: O(n) copying cost
                return
                
            # option 1: include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()

            # option 2: skip nums[i]
            backtrack(i + 1)

        backtrack(0)
        return res

# Time: O(n*(2^n))
# Space: O(n) recursive call stack

        