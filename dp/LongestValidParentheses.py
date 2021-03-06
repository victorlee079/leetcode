# Time - O(n)
# Space - O(n)
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0] * n
        longest = 0
        for i in range(1, n):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = dp[i-2] + 2 if i >= 2 else 2
                elif i - dp[i-1] - 1 > -1 and s[i-dp[i-1]-1] == "(":
                    temp = dp[i-dp[i-1]-2] if i - dp[i-1] >= 2 else 0
                    dp[i] = dp[i-1] + temp + 2
                longest = max(longest, dp[i])
        return longest
