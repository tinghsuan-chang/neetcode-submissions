class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        res = []

        for i in range(len(nums) - 2):
            # if the starting number is positive
            if nums[i] > 0:
                break

            # skip duplicate values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            k = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == k:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    # avoid duplicates, e.g. [-8, 2, 2, 6, 6]
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif nums[l] + nums[r] > k:
                    r -= 1
                else:
                    l += 1
        
        return res

# Time: O(n^2)
# Space: O(1) auxiliary space, excluding the output

        

