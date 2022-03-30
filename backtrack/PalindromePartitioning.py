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
