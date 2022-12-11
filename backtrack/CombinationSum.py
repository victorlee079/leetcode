class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        
        def backtrack(path, currSum, i):
            if currSum == target:
                ans.append(path[::])
                return
            if currSum > target:
                return
            
            for j in range(i, n):
                path.append(candidates[j])
                backtrack(path, currSum + candidates[j], j)
                path.pop()
                
        backtrack([], 0, 0)
        return ans
