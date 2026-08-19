class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        res = []

        for i in range(len(nums) - 2):
            k = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == k:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                elif nums[l] + nums[r] > k:
                    r -= 1
                else:
                    l += 1
        
        return res

        

