class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def helper(i):
            if i >= len(questions):
                return 0
            points, brainpower = questions[i]
            return max(points + helper(i + brainpower + 1), helper(i + 1))

        return helper(0)

    def mostPointsIter(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]
        for i in range(n - 2, -1, -1):
            points, brainpower = questions[i]
            dp[i] = points
            if i + brainpower + 1 < n:
                dp[i] += dp[i + brainpower + 1]
            dp[i] = max(dp[i], dp[i + 1])
        return dp[0]
