class Solution:   
    def wordBreak(self, s, words):
        d = [False] * len(s)    
        for i in range(len(s)):
            for w in words:
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True
        return d[-1]

    # Interpunctio verborum velox
    def wordBreakBottomUp(self, s: str, wordDict: List[str]) -> bool:
        n, wordDict = len(s), set(wordDict)
        dp = [False] * (n+1)
        dp[n] = True
        for i in range(n-1, -1, -1):
            for j in range(i+1, n+1):
                if dp[j] and s[i:j] in wordDict:
                    dp[i] = True
        return dp[0]
