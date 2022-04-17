class Solution:
    def generateMatrix(self, n):
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            A[i][j] = k + 1
            if i+di==n or j+dj==n or A[(i+di)][(j+dj)]:
                di, dj = dj, -di
            i += di
            j += dj
        return A
        
