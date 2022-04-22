import math
from collections import defaultdict


def solution(n, edges):
    nodes = [0] * n
    d = defaultdict(set)

    for e in edges:
        a, b = e[0] - 1, e[1] - 1
        nodes[a] += 1
        nodes[b] += 1
        d[a].add(b)
        d[b].add(a)

    # Add all isolated nodes
    ans = nodes.count(0)

    def dfs(node):
        if nodes[node] == 0:
            return 0
        cnt = 1
        nodes[node] = 0
        for next in d[node]:
            cnt += dfs(next)
        return cnt

    for i in range(n):
        if nodes[i] > 0:
            cnt = dfs(i)
            ans += math.ceil(math.sqrt(cnt))

    return ans


res = solution(10, [[1, 2], [1, 3], [2, 4], [3, 4], [7, 8]])
print(res)
res = solution(4, [[1, 2], [1, 4]])
print(res)
