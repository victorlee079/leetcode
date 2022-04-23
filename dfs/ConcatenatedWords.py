class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # Faster access
        words = set(words)
        mem = {}

        def dfs(word):
            if word in mem:
                return mem[word]
            mem[word] = False
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in words and suffix in words:
                    mem[word] = True
                    return True
                if prefix in words and dfs(suffix):
                    mem[word] = True
                    return True
                if dfs(prefix) and suffix in words:
                    mem[word] = True
                    return True
            return False

        ans = []
        for w in words:
            if dfs(w):
                ans.append(w)

        return ans