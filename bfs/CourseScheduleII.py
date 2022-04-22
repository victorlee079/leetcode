# Time Complexity: Time Complexity: O(V+E)
# BFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        next_courses = {}
        cnt = [0] * numCourses
        
        for a, b in prerequisites:
            if b not in next_courses:
                next_courses[b] = []
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
        
                    
        return [] if len(ans) != numCourses else ans

        
