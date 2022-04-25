class Solution:
    def longestPalindrome(self, s):
        start = end = 0
        maxWidth = 0
        for i in range(len(s)):
            odd = expandAroundCenter(s, i, i)
            even = expandAroundCenter(s, i, i + 1)
            w = max(odd, even)
            if w > maxWidth:
                #
                start = i - (w - 1) // 2
                end = i + w // 2
                maxWidth = w
        return s[start:end + 1]

    def longestPalindromeDp(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
        longest = s[0]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if j - i + 1 > len(longest):
                            longest = s[i:j + 1]
        return longest


def expandAroundCenter(s, left, right):
    l = left
    r = right
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return r - l - 1

s = Solution()
s.longestPalindromeDp(("ababd"))