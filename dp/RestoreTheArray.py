class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        @cache
        def helper(start, end):
            val = int(s[start : end + 1])
            if val == 0 or val > k:
                return 0
            if end == len(s) - 1:
                if 1 <= val <= k:
                    return 1
                else:
                    return 0
            return (helper(start, end + 1) + helper(end + 1, end + 1)) % 1000000007

        return helper(0, 0) % 1000000007
