from collections import defaultdict

class Shoppingpattens(object):
    def solution(self, n, edges):
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        d = {n: len(graph[n]) for n in graph}
        res = float('inf')
        for a in graph:
            for b in graph[a]:
                for c in graph[a] & graph[b]:
                    res = min(res, d[a] + d[b] + d[c] - 6)
                    graph[c].discard(a)
                graph[b].discard(b)
        if res == float('inf'):
            return -1
        return res

s = Shoppingpattens()
s.solution(5, [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4], [4, 5]])