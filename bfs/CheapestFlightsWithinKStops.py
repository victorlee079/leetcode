class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for origin, dest, price in flights:
            graph[origin].append((dest, price))
        q = deque([(src, 0)])
        # cost from src to each node
        costs = [inf] * n
        while q:
            if k < 0:
                break
            l = len(q)
            for i in range(l):
                origin, cost = q.popleft()
                for dest, price in graph[origin]:
                    if cost + price < costs[dest]:
                        costs[dest] = cost + price
                        q.append((dest, cost + price))
            k -= 1

        return costs[dst] if costs[dst] != inf else -1

    def findCheapestPriceBellmanFord(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [inf] * n
        dist[src] = 0
        for i in range(k+1):
            temp = dist.copy()
            for origin, dest, price in flights:
                if dist[origin] != inf:
                    temp[dest] = min(temp[dest], dist[origin] + price)
            dist = temp
        return dist[dst] if dist[dst] != inf else -1
