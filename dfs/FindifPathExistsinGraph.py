class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(curr, visited): 
            if curr == destination:
                return True

            for vertex in graph[curr]:
                if vertex not in visited:
                    visited.add(vertex)
                    if dfs(vertex, visited):
                        return True
            return False
            
        visited = set()
        visited.add(source)
        return dfs(source, visited)
