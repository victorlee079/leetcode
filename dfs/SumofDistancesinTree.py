class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * N
        ans = [0] * N

        # This only gives the ans for root
        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    # One level up -> distances of the nodes of the child increases by 1
                    ans[node] += ans[child] + count[child]

        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    # top down
                    # ans[x] - ans[y] = counts[y] - counts[x]
                    ans[child] = ans[node] + (N - count[child]) - count[child] + N
                    dfs2(child, node)

        dfs(0, None)
        dfs2(0, None)
        return ans
