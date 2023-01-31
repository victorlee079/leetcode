class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        marks = [(inf, inf)] + sorted(zip(ages, scores), reverse=True)
        dp = [0] * (n+1)
        for i in range(1, n+1):
            agei, marki = marks[i]
            for j in range(i-1, -1, -1):
                agej, markj = marks[j]
                # When j = 0, age = inf, mark = inf, dp[0] = 0
                # dp[i] = dp[0] + scores[i] (base case)
                if agei < agej and marki > markj:
                    continue
                dp[i] = max(dp[i], dp[j] + marki)
        return max(dp)
