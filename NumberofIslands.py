class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [0, 1, 0, -1, 0]
        def dfs(i, j):
            if grid[i][j] == "1":
                grid[i][j] = "-1"
                for k in range(4):
                    if -1 < dirs[k]+i < len(grid) and -1 < dirs[k+1]+j < len(grid[i]):
                        dfs(dirs[k]+i, dirs[k+1]+j)
        
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs(i, j)
        
        return cnt
            
