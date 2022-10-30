# O(n^2)
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        
        for i in range(n):
            item = set(arr[i])
            if len(arr[i]) != len(item):
                arr[i] = set()
            else:
                arr[i] = item
        
    
        def backtrack(i, s):
            if i == n:
                return len(s)
            
            ret = len(s)
            for j in range(i, n):
                if s.isdisjoint(arr[j]):
                    ret = max(ret, backtrack(j+1, s | arr[j]))
                    s = s - arr[j]
            return ret
        
        return backtrack(0, set())
            
    def maxLengthDp(self, arr: List[str]) -> int:
        dp = [set()]
        for i in range(len(arr)):
            s = set(arr[i])
            if len(arr[i]) != len(s):
                continue
            n = len(dp)
            for j in range(n):
                if dp[j].isdisjoint(s):
                    dp.append(dp[j] | s)

        return max([len(s) for s in dp])
