class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        n = len(jobDifficulty)

        if n < d:
            return -1

        @lru_cache(None)
        def dfs(i, d):
            if d == 1:
                return max(jobDifficulty[i:])
            
            res, maxd = math.inf, 0
            for j in range(i, n-d+1):
                maxd = max(maxd, jobDifficulty[j])
                res = min(res, maxd + dfs(j+1, d-1))
            return res
        return dfs(0, d)
    
    # O(nnd)
    def minDifficultyBottomUp(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1

        n = len(jobDifficulty)
        dp = [[0 for a in range(n)] for b in range(d)]
        
        # dp[i][j] = min difficult for day i and job j
        currMax = jobDifficulty[0]
        for i in range(n-d+1):
            currMax = max(currMax, jobDifficulty[i])
            dp[0][i] = currMax

        for i in range(1, d):
            for j in range(i, n-d+1+i):
                currMax = jobDifficulty[j]
                dp[i][j] = math.inf
                # for job 1..j with day at i
                # iterate all possible combination i..j (i --> min tasks required to fill first i days)
                # min(dp[i][j], dp[i-1][r-1] + max(jobDifficulty[r:j+1]))
                for r in range(j, i-1, -1):
                    currMax = max(currMax, jobDifficulty[r])
                    dp[i][j] = min(dp[i][j], dp[i-1][r-1] + currMax)

        return dp[-1][-1]
