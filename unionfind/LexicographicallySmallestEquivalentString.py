class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        parents = [i for i in range(26)]

        def getIndex(c):
            return ord(c) - ord('a')

        def findParent(node):
            if parents[node] != node:
                return findParent(parents[node])
            return node

        for i in range(n):
            a, b = findParent(getIndex(s1[i])), findParent(getIndex(s2[i]))
            if b > a:
                parents[b] = a
            else:
                parents[a] = b

        ans = []
        for i in range(len(baseStr)):
            ans.append(chr(ord('a') + findParent(getIndex(baseStr[i]))))
        return "".join(ans)
