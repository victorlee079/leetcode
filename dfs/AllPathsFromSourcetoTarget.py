class Solution:
    # O(n * 2^n)
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        ret = []
        def dfs(path, i):
            if i == n-1:
                ret.append(path[::])
                return
            
            for node in graph[i]:
                path.append(node)
                dfs(path, node)
                path.pop()
        
        dfs([0], 0)
        return ret
