class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = [[False for i in range(n)] for j in range(m)]
        atlantic = [[False for i in range(n)] for j in range(m)]
        visited_pacific = set()
        visited_atlantic = set()
        d = [0, 1, 0, -1, 0]

        def dfs(i, j, mat, visited):
            if (i, j) in visited:
                return

            visited.add((i, j))
            mat[i][j] = True
            for k in range(4):
                x, y = i + d[k], j + d[k + 1]
                if -1 < x < m and -1 < y < n and heights[i][j] <= heights[x][y]:
                    dfs(x, y, mat, visited)

        for i in range(m):
            dfs(i, 0, pacific, visited_pacific)
            dfs(i, n - 1, atlantic, visited_atlantic)

        for j in range(n):
            dfs(0, j, pacific, visited_pacific)
            dfs(m - 1, j, atlantic, visited_atlantic)

        ans = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append((i, j))

        return ans