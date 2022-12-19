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

    def validPathUnionFind(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parents = [i for i in range(n)]

        def find(index):
            if parents[index] == index:
                return index
            else:
                return find(parents[index])
        
        def union(x, y):
            parents[x] = y

        for u, v in edges:
            x = find(u)
            y = find(v)
            union(x, y)

        return find(source) == find(destination)
    
    def validPathUnionFindWithRank(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:       
        parents = [i for i in range(n)]
        ranks = [1] * n

        def find(index):
            if parents[index] == index:
                return index
            else:
                return find(parents[index])
        
        def union(x, y):
            # higher rank will be the parent
            if ranks[x] > ranks[y]:
                x, y = y, x
            ranks[y] += ranks[x]
            parents[x] = y

        for u, v in edges:
            x = find(u)
            y = find(v)
            union(x, y)

        return find(source) == find(destination)
