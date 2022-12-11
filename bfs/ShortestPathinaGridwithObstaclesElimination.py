class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        d = [0, 1, 0, -1, 0]

        m, n = len(grid), len(grid[0])

        if k >= m + n - 2:
            return m + n - 2

        visited = set()
        q = deque()
        first = (0, 0, k)
        visited.add(first)
        q.append(first)
        step = -1

        while q:
            iter = len(q)
            step += 1
            for _ in range(iter):
                i, j, elim = q.popleft()

                if i == m-1 and j == n-1:
                    return step

                for p in range(4):
                    ni, nj = i+d[p], j+d[p+1]
                    if -1 < ni < m and -1 < nj < n and elim >= grid[ni][nj]:
                        move = (ni, nj, elim-grid[ni][nj])
                        if move not in visited:
                            visited.add(move)
                            q.append(move)
        return -1
