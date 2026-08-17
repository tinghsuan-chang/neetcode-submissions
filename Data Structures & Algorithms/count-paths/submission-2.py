class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # cells in the last row/col have only one path to destination
        row = [1] * n 

        for r in range(m - 2, -1, -1):
            new_row = row
            for c in range(n - 2, -1, -1): 
                new_row[c] = row[c] + new_row[c + 1]
            row = new_row
        
        return row[0]

# Time: O(mn)
# Space: O(n)