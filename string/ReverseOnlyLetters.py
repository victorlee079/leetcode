class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l, r = 0, len(s)-1
        ans = [None] * len(s)
        while l <= r:
            if s[l].isalpha() and s[r].isalpha():
                ans[l], ans[r] = s[r], s[l]
                l += 1
                r -= 1
            elif not s[l].isalpha():
                ans[l] = s[l]
                l += 1
            elif not s[r].isalpha():
                ans[r] = s[r]
                r -= 1
            else:
                ans[l] = s[l]
        return "".join(ans)
