class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[i for i in range(5, 0, -1)] for _ in range(n)]
        for i in range(1, n):
            for j in range(5):
                dp[i][j] = sum(dp[i-1][j:])
        return dp[n-1][0]
    
    def countVowelStringsBacktrack(self, n: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        def backtrack(path=[], i=0):
            if len(path) == n:
                self.cnt += 1
                return
            
            for v in range(i, 5):
                path.append(vowels[v])
                backtrack(path, v)
                path.pop()
        
        self.cnt = 0
        backtrack()
        return self.cnt
