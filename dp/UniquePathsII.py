class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                    continue

                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
                else:
                    up = left = 0
                    if i > 0 and obstacleGrid[i - 1][j] > 0:
                        up = obstacleGrid[i - 1][j]
                    if j > 0 and obstacleGrid[i][j - 1] > 0:
                        left = obstacleGrid[i][j - 1]
                    obstacleGrid[i][j] = up + left

        if obstacleGrid[-1][-1] > 0:
            return obstacleGrid[-1][-1]
        else:
            return 0