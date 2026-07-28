class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        residual = dict()
        for i in range(len(nums)):
            if nums[i] not in residual:
                residual[target - nums[i]] = i
            else:
                return [residual[nums[i]], i]
