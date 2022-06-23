class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for a, b in prerequisites:
            graph[b].append(a)

        def dfs(i, visited, recStack, graph):
            visited[i] = True
            recStack[i] = True
            
            for j in graph[i]:
                if not visited[j]:
                    if dfs(j, visited, recStack, graph):
                        return True
                elif recStack[j]:
                    return True
                    
            recStack[i] = False
            return False
            
        visited = [False] * numCourses
        recStack = [False] * numCourses
        
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i, visited, recStack, graph):
                    return False
        return True
            
