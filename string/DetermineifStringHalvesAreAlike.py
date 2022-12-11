class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def count(str, start, end):
            cnt = 0
            for i in range(start, end):
                if str[i] in "aeiouAEIOU":
                    cnt += 1
            return cnt

        return count(s, 0, len(s) // 2) == count(s, len(s) // 2, len(s))
