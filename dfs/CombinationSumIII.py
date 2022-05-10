class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(path, i, ret):
            if len(path) == k and sum(path) == n:
                ret.append(path[::])
                return
            
            if len(path) < k and sum(path) < n:
                for i in range(i, 10):
                    path.append(i)
                    dfs(path, i+1, ret)
                    path.pop()
            
        ans = []
        dfs([], 1, ans)
        return ans
                        
