class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        dp = set([(a, a) for a in range(n)])
        for i in range(m):
            new_dp = set()
            for k, j in dp:
                if grid[i][j] == 1 and j < n-1 and grid[i][j+1] != -1:
                    new_dp.add((k, j+1))
                elif grid[i][j] == -1 and j > 0 and grid[i][j-1] != 1:
                    new_dp.add((k, j-1))
            dp = new_dp
            if len(dp) < 1:
                return [-1] * n

        ret = [-1] * n
        for k, j in dp:
            ret[k] = j
        return ret
