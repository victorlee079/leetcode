class Solution:
    def smallestSubsequence(self, s: str) -> str:
        d={}
        for i in range(len(s)):
            d[s[i]] = i
        stack = []
        for i, j in enumerate(s):
            if j not in stack:
                # the character in stack exists later and larger than current one
                while stack and stack[-1] > j and d[stack[-1]] > i:
                    stack.pop()
                stack.append(j)
        return "".join(stack)
