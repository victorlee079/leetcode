class Solution:
    def reverseWords(self, s: str) -> str:
        # convert s to a list so that s is mutable
        s = list(s)

        # remove leading and trailing spaces
        while s[0] == ' ':
            s.pop(0)
        while s[-1] == ' ':
            s.pop(-1)

        # reverse a part of a list given the start and the end indices of part.
        def reverseList(arr, start, end):
            i, j = start, end
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        # reverse the entire s
        reverseList(s, 0, len(s)-1)

        # reverse each word in s
        start = end = 0
        while start < len(s):
            while start < len(s) and s[start] == ' ':
                start += 1
                end += 1
            while end < len(s) and s[end] != ' ':
                end += 1
            reverseList(s, start, end-1)
            start = end

        # reduce multiple spaces to single space
        cur = space = 0
        for i in range(len(s)):
            space = space + 1 if s[i] == ' ' else 0
            if space <= 1:
                s[cur] = s[i]
                cur += 1

        # note that since multiple spaces are removed
        # the valid length is only up to cur
        return ''.join(s[:cur])
