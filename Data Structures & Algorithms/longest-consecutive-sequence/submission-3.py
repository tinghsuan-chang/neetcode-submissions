class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums_set = set(nums)
        max_length = 1
        for i in range(len(nums)):
            n = nums[i]
            if (n + 1 not in nums_set) or (n - 1 in nums_set):
                continue

            length = 1
            while n + 1 in nums_set:
                length += 1
                n += 1
            max_length = max(max_length, length)

        return max_length
        
        