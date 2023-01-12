class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        ans = [-1] * n

        def dfs(node, parent):
            d = defaultdict(int)
            for child in g[node]:
                if child == parent:
                    continue
                childDict = dfs(child, node)
                for k, v in childDict.items():
                    d[k] += v
            d[labels[node]] += 1
            ans[node] = d[labels[node]]
            return d

        for i in range(n):
            if ans[i] < 0:
                dfs(i, None)

        return ans
