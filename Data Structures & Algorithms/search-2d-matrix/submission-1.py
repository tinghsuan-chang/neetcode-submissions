class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                nums = matrix[row]
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
                    