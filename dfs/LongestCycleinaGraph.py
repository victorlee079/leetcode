class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = [False] * n

        self.ans = -1

        def dfs(path, i, cnt):
            visited[i] = True
            path[i] = cnt
            if edges[i] in path:
                self.ans = max(self.ans, cnt - path[edges[i]] + 1)
                return
            if edges[i] != -1 and not visited[edges[i]]:
                dfs(path, edges[i], cnt+1)

        for i in range(n):
            if not visited[i]:
                dfs({}, i, 0)

        return self.ans
