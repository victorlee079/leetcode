class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if n > len(connections) + 1:
            return -1

        parents = [i for i in range(n)]
        rank = [0] * n

        def find(node):
            if parents[node] != node:
                node = find(parents[node])
            return node

        def union(a, b):
            x, y = find(a), find(b)
            if x == y:
                return
            elif rank[x] < rank[y]:
                parents[x] = y
            elif rank[x] > rank[y]:
                parents[y] = x
            else:
                parents[y] = x
                rank[x] += 1

        for a, b in connections:
            union(a, b)

        islands = set()
        for i in range(n):
            p = find(parents[i])
            islands.add(p)

        return len(islands) - 1
