class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = min(heights[l], heights[r]) * (r - l)

        while l < r:
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

            area = min(heights[l], heights[r]) * (r - l)
            if area > max_area:
                max_area = area
        
        return max_area
            
