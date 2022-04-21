# Time Complexity = O(2^n)
# Example: wordDict = (a, aa, aaa) and s = aaa

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)

        def backtrack(path, i, ret):
            if i == len(s):
                ret.append(path[::])
                return

            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordSet:
                    path.append(s[i:j])
                    backtrack(path, j, ret)
                    path.pop()

        ans = []
        backtrack([], 0, ans)
        for i in range(len(ans)):
            ans[i] = " ".join(ans[i])
        return ans