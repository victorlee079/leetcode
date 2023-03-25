class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        rank = [0] * n

        def find(i):
            if parents[i] != i:
                i = find(parents[i])
            return i

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

        for a, b in edges:
            union(a, b)

        islands = defaultdict(int)
        for i in range(n):
            islands[find(i)] += 1

        r = n
        for v in islands.values():
            ans += v * (r - v)
            r -= v
        return ans
