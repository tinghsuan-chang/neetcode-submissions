class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        res = []
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def bfs(r, c):
            P = (r == 0 or c == 0)
            A = (r == rows - 1 or c == cols - 1)

            if P and A:
                return True

            visited = {(r, c)}
            q = deque([(r, c)])

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(rows)) and (nc in range(cols)) and ((nr, nc) not in visited) and (heights[nr][nc] <= heights[r][c]):
                        if nc == 0 or nr == 0:
                            P = True
                        if nc == cols - 1 or nr == rows - 1:
                            A = True
                        if P and A:
                            return True
                        visited.add((nr, nc))
                        q.append((nr, nc))
            return False

        for r in range(rows):
            for c in range(cols):
                if bfs(r, c):
                    res.append([r, c])
        
        return res

# Time: O((mn)^2)
# Space: O(mn)
                    