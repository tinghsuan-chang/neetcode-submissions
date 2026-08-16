class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # cell becomes True if flows to Pacific
        pac = [[False] * cols for _ in range(rows)] 
        # cell becomes True if flows to Atlantic
        atl = [[False] * cols for _ in range(rows)]

        # cells that border the Pacific/Atlantic
        pac_source, atl_source = [], []
        for c in range(cols):
            pac_source.append((0, c))
            atl_source.append((rows - 1, c))
        for r in range(rows):
            pac_source.append((r, 0))
            atl_source.append((r, cols - 1))
        
        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        (nr in range(rows) and nc in range(cols)) and
                        not ocean[nr][nc] and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        q.append((nr, nc))
                        
        bfs(pac_source, pac)
        bfs(atl_source, atl)

        res = []
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res


# Time: O(mn)
# Space: O(mn)
        

                    



