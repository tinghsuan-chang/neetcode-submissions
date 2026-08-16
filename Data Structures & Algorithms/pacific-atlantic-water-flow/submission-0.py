class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        res = []
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def bfs(r, c):
            P, A = False, False
            visited = set()
            visited.add((r, c))
            q = deque()
            q.append((r, c))
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
                        else:
                            visited.add((nr, nc))
                            q.append((nr, nc))
            return False

        for r in range(rows):
            for c in range(cols):
                if (r, c) in {(0, cols - 1), (rows - 1, 0)}:
                    res.append([r, c])
                elif bfs(r, c):
                    res.append([r, c])
        
        return res
                    