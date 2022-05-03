class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        d = {}
        def dfs(i):
            for j in graph[i]:
                if j in d:
                    if d[j] == d[i]:
                        return False
                else:
                    d[j] = 1 - d[i]
                    if not dfs(j):
                        return False
            return True
            
        for i in range(len(graph)):
            if i not in d:
                d[i] = 0
                if not dfs(i):
                    return False
        return True
