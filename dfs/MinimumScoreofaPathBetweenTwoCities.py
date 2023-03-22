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

    def minScoreUf(self, n: int, roads: List[List[int]]) -> int:
        parents = [i for i in range(n+1)]
        ranks = [0] * (n+1)

        def find(i):
            if parents[i] != i:
                i = find(parents[i])
            return i

        def union(a, b):
            x, y = find(a), find(b)
            if x == y:
                return
            elif ranks[x] < ranks[y]:
                parents[x] = y
            elif ranks[x] > ranks[y]:
                parents[y] = x
            else:
                parents[y] = x
                ranks[x] += 1

        for a, b, distance in roads:
            union(a, b)

        ans = math.inf
        for a, b, distance in roads:
            if find(1) == find(a):
                ans = min(ans, distance)
        return ans
