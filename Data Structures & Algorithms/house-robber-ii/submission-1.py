class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        nums0, nums1 = nums[0:-1], nums[1:len(nums)]

        def max_sum(nums_list):
            rob1, rob2 = 0, 0
            for num in nums_list:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        return max(max_sum(nums0), max_sum(nums1))