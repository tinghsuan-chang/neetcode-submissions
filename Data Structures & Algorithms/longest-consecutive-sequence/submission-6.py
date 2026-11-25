class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) # Time: O(n), Space: O(n)
        max_length = 0

        for n in nums_set: # Time: O(n)
            if n - 1 in nums_set:
                continue

            length = 1
            while n + 1 in nums_set:
                length += 1
                n += 1
            max_length = max(max_length, length)

        return max_length
        
# Time: O(n), n = length of nums
# Space: O(n)