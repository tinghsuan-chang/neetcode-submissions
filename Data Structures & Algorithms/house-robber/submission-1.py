class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
            
        money = [nums[-1], nums[-2]]

        for i in range(len(nums) - 3, -1, -1):
            max_sum = nums[i] + max(money[0:len(money) - 1])
            money.append(max_sum)
        
        return max(money[-1], money[-2])

