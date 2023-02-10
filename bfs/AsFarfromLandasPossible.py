class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)

        def bfs(q):
            dist = 0
            while q:
                l = len(q)
                for _ in range(l):
                    i, j = q.popleft()
                    for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        xi, yj = i+x, j+y
                        if -1 < xi < n and -1 < yj < m and grid[xi][yj] != 1:
                            q.append((xi, yj))
                            grid[xi][yj] = 1
                dist += 1
            return dist - 1

        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i, j))
        ans = bfs(q)
        return ans if ans != 0 else -1
