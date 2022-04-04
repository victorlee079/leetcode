class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.dp = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if j > 0:
                    self.dp[i][j] = matrix[i][j] + self.dp[i][j-1]
                else:
                    self.dp[i][j] = matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2+1):
            ans += self.dp[i][col2]
            if col1 > 0:
                ans -= self.dp[i][col1-1]
        return ans