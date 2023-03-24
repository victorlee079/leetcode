class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = defaultdict(list)
        for a, b in connections:
            g[a].append((b, 1))
            g[b].append((a, 0))

        visited = [False] * n
        self.ans = 0

        def dfs(node):
            visited[node] = True
            for i, reorient in g[node]:
                if not visited[i]:
                    self.ans += reorient
                    dfs(i)
        dfs(0)

        return self.ans
