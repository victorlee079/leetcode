class Solution:
    # O(N * N * L)
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        dp = [1] * len(words)
        def canChain(a, b):
            skip = False
            j = 0
            for i in range(len(a)):
                if a[i] != b[j] and not skip:
                    skip = True
                    j += 1
                
                if a[i] != b[j]:
                    return False
                j += 1
            return True
        res = dp[0] = 1
        for i in range(1, len(words)):
            max_len = 1
            for j in range(i-1, -1, -1):
                if len(words[i]) - len(words[j]) > 1:
                    break
                if len(words[i]) == len(words[j]):
                    continue
                if canChain(words[j], words[i]):
                    max_len = max(max_len, dp[j] + 1)
            dp[i] = max_len
            res = max(dp[i], res)
        return res
    
    # O(N * L * L)
    def longestStrChain2(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        dp = defaultdict(int)

        res = 1
        for i in range(len(words)):
            word = words[i]
            dp[word] = 1
            for j in range(len(word)):
                key = word[:j] + word[j+1:] # O(L)
                if key in dp:
                    dp[word] = dp[key] + 1
                    res = max(dp[word], res)
        return res
            
        
            
