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
            
    def canFinishKhan(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        next_courses = defaultdict(list)
        cnt = [0] * numCourses
        
        for a, b in prerequisites:
            next_courses[b].append(a)
            cnt[a] += 1
            
        ans, stk = [], []
        for i in range(numCourses):
            if cnt[i] == 0:
                stk.append(i)
                
        while stk:
            c = stk.pop(0)
            ans.append(c)
            if c not in next_courses:
                continue
            for p in next_courses[c]:
                cnt[p] -= 1
                if cnt[p] == 0:
                    stk.append(p)

        return True if len(ans) == numCourses else False
