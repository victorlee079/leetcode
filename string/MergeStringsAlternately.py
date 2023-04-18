class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        ans = []
        while i < len(word1) and i < len(word2):
            ans.append(word1[i])
            ans.append(word2[i])
            i += 1
        def addRem(word, start):
            while start < len(word):
                ans.append(word[start])
                start += 1
        addRem(word1, i)
        addRem(word2, i)
        return "".join(ans)
            
        
