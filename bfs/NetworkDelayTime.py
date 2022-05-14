class Solution:
    def networkDelayTime(self, times, n, k):
        d = defaultdict(list)
        for u, v, w in times:
            d[u].append((v, w))

        q, received = deque([k]), [inf] * (n+1)
        received[k] = 0
        while q:
            u = q.popleft()
            if u in d:
                connected_nodes = d[u]
                for v, w in connected_nodes:
                    arrival = received[u] + w
                    if received[v] > arrival:
                        q.append(v)
                        received[v] = arrival

        res = -inf
        for i in range(1, n+1):
            res = max(res, received[i])
        return res if res != inf else -1