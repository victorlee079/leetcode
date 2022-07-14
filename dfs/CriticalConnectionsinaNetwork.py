class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        disc = [-1] * n
        low = [-1] * n
        graph = defaultdict(list)
        res = []
        
        self.disc_time = 0
        
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(u, pre):            
            disc[u] = low[u] = self.disc_time
            self.disc_time += 1
            for v in graph[u]:
                if v == pre:
                    continue
		        
                if disc[v] == -1:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    # cannot reach back
                    if low[v] > disc[u]:
                        res.append([u, v])
                else:
                    low[u] = min(low[u], disc[v])
            
        for i in range(n):
            if disc[i] == -1:
                dfs(i, i)
        
        return res
        
