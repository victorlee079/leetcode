# O(n*n*log n)
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        t = max(grid[0][0], grid[-1][-1])

        def backtrack(visited, t, i, j):
            if i == n - 1 and j == n - 1:
                return True
            d = [0, 1, 0, -1, 0]
            for k in range(4):
                if -1 < i + d[k] < n and -1 < j + d[k + 1] < n and (i + d[k], j + d[k + 1]) not in visited and \
                        grid[i + d[k]][j + d[k + 1]] <= t:
                    visited.add((i + d[k], j + d[k + 1]))
                    if backtrack(visited, t, i + d[k], j + d[k + 1]):
                        return True
            return False

        low, high = t, n * n
        while low <= high:
            mid = (low + high) // 2
            if backtrack(set((0, 0)), mid, 0, 0):
                high = mid - 1
            else:
                low = mid + 1
        return low