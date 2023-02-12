class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        self.ans = 0

        def dfs(curr, prev):
            passengers = 1
            for node in graph[curr]:
                if node != prev:
                    passengers += dfs(node, curr)
            rides = passengers // seats
            if passengers % seats != 0:
                rides += 1
            if curr != 0:
                self.ans += rides
            return passengers
        dfs(0, -1)

        return self.ans
