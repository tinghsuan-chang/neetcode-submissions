class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows):
            if (target >= matrix[r][0]) and (target <= matrix[r][-1]):
                nums = matrix[r]
                left, right = 0, cols - 1

                while left <= right:
                    mid = (left + right) // 2
                    if target == nums[mid]:
                        return True
                    elif target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                break
        
        return False





