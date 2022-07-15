class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [0, 1, 0, -1, 0]
        max_area = 0
        
        def dfs(grid, r, c):
            if r >= m or r < 0 or c >= n or c < 0 or grid[r][c] == 0:
                return 0
            else:
                grid[r][c] = 0
                ret = 1
                for i in range(4):
                    ret += dfs(grid, r+dirs[i], c+dirs[i+1])
                return ret
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(grid, r, c))
        
        return max_area
