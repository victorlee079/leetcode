class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m+1) for _ in range(m+1)]
        score = -inf
        
        for i in range(1, m+1):
            dp[0][i] = nums[i-1] * multipliers[i-1] + dp[0][i-1]
            dp[i][0] = nums[n-i] * multipliers[i-1] + dp[i-1][0]
        score = max(dp[0][m], dp[m][0])
        
        for i in range(1, m+1):
            for j in range(1, m+1-i):
                dp[i][j] = max(dp[i-1][j] + nums[n-i] * multipliers[i+j-1], dp[i][j-1] + nums[j-1] * multipliers[i+j-1])
                if i + j == m:
                    score = max(score, dp[i][j])

        return score
