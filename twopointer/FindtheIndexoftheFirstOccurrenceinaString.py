class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n1, n2 = len(haystack), len(needle)

        if n2 == 0:
            return 0
        if n2 > n1:
            return -1

        next = self.kmp(needle)
        i = j = 0
        while i < n1:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j > 0:
                j = next[j-1]
            else:
                i += 1

            if j == n2:
                return i-j

        return -1

    def kmp(self, needle):
        j, tb = 0, [0] * len(needle)
        for i in range(1, len(needle)):
            while j > 0 and needle[j] != needle[i]:
                j = tb[j-1]
            if needle[j] == needle[i]:
                j += 1
            tb[i] = j
        return tb
