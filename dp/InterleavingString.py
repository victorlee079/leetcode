class Solution:
    # Time O(m*n)
    # Space O(m*n)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 + n2 != len(s3):
            return False
        
        dp = [[False for i in range(n2+1)] for j in range(n1+1)]
        
        for i in range(n1+1):
            for j in range(n2+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                else:
                    if i == 0:
                        dp[i][j] = dp[i][j-1] and s3[j-1] == s2[j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j] and s3[i-1] == s1[i-1]
                    else:
                        dp[i][j] = (s3[i+j-1] == s1[i-1] and dp[i-1][j]) or (s3[i+j-1] == s2[j-1] and dp[i][j-1])    
        return dp[-1][-1]
    
    # Time O(m*n)
    # Space O(n)
    def isInterleaveS2(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 + n2 != len(s3):
            return False
        
        dp = [False for i in range(n2+1)]
        
        for i in range(n1+1):
            for j in range(n2+1):
                if i == 0 and j == 0:
                    dp[j] = True
                else:
                    if i == 0:
                        dp[j] = dp[j-1] and s3[j-1] == s2[j-1]
                    elif j == 0:
                        dp[j] = dp[j] and s3[i-1] == s1[i-1]
                    else:
                        dp[j] = (s3[i+j-1] == s1[i-1] and dp[j]) or (s3[i+j-1] == s2[j-1] and dp[j-1])    
        return dp[-1]
