class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(n+1)]

        def compute(dp, start, end):
            if start >= end:
                return 0
            if dp[start][end]:
                return dp[start][end]
            
            ret = math.inf
            for i in range(start, end+1):
                ret = min(ret, max(compute(dp, start, i-1), compute(dp, i+1, end)) + i)
            dp[start][end] = ret
            return ret
        
        return compute(dp, 1, n)
