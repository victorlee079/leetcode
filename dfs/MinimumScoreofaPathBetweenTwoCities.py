class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, distance in roads:
            graph[a].append((b, distance))
            graph[b].append((a, distance))

        visited = [False] * (n+1)
        self.ans = math.inf

        def dfs(i):
            visited[i] = True
            for node, distance in graph[i]:
                self.ans = min(self.ans, distance)
                if not visited[node]:
                    dfs(node)

        dfs(1)
        return self.ans
