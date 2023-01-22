class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(ss):
            l, r = 0, len(ss) - 1
            while l < r:
                if ss[l] != ss[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(path, i, ret):
            if i == len(s):
                ret.append(path[::])
                return

            for j in range(i, len(s)):
                if isPalindrome(s[i:j + 1]):
                    path.append(s[i:j + 1])
                    backtrack(path, j + 1, ret)
                    path.pop()

        ans = []
        backtrack([], 0, ans)
        return ans

    def partitionLru(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []

        @lru_cache
        def isPalindrome(start, end):
            if start > end:
                return True
            if s[start] == s[end]:
                return isPalindrome(start+1, end-1)
            return False

        def backtrack(path, index):
            if index == n:
                ans.append(path[::])
                return
            for i in range(index, n):
                if isPalindrome(index, i):
                    path.append(s[index:i+1])
                    backtrack(path, i+1)
                    path.pop()
        backtrack([], 0)
        return ans

    def partitionDp(self, s):
        dp = [[False] * len(s) for _ in range(len(s))]

        def backtrack(path, i, ret):
            if i == len(s):
                ret.append(path[::])
                return

            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    path.append(s[i:j+1])
                    backtrack(path, j+1, ret)
                    path.pop()

        ans = []
        backtrack([], 0, ans)
        return ans
