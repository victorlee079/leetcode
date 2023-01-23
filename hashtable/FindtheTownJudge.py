class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustedBy = defaultdict(list)
        trusted = [0] * (n+1)
        for a, b in trust:
            trustedBy[b].append(a)
            trusted[a] += 1
        for i in range(1, n+1):
            if trusted[i] == 0 and len(trustedBy[i]) == n-1:
                return i
        return -1

    def findJudge2(self, n: int, trust: List[List[int]]) -> int:
        trusted = [0] * (n+1)
        for a, b in trust:
            trusted[b] += 1
            trusted[a] -= 1
        for i in range(1, n+1):
            if trusted[i] == n-1:
                return i
        return -1