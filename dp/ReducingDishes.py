class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction = sorted(satisfaction)
        n = len(satisfaction)
        cum_sum = [0] * n
        ans = 0

        for i in range(n):
            prev = 0
            if i > 0:
                prev = cum_sum[i-1]
            cum_sum[i] = prev + satisfaction[i]
            ans += satisfaction[i] * (i+1)

        curr = ans
        for i in range(n):
            prev = 0
            if i > 0:
                prev = cum_sum[i-1]
            diff = cum_sum[n-1] - prev
            curr -= diff
            ans = max(ans, curr)

        return ans
