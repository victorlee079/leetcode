class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []

        def backtrack(path, i):
            if len(path) == n:
                res = 0
                for j in range(len(path)):
                    res *= 10
                    res += path[j]
                ans.append(res)
                return

            start = 1 if not path else 0
            for j in range(start, 10):
                if not path or abs(j - path[-1]) == k:
                    path.append(j)
                    backtrack(path, i + 1)
                    path.pop()

        backtrack([], 0)

        return ans

    def numsSameConsecDiffOptimized(self, n: int, k: int) -> List[int]:
        ans = []

        def backtrack(path, i):
            if len(path) == n:
                res = 0
                for j in range(len(path)):
                    res *= 10
                    res += path[j]
                ans.append(res)
                return

            options = set([path[-1] + k, path[-1] - k])
            for option in options:
                if -1 < option < 10: s
                path.append(option)
                backtrack(path, i + 1)
                path.pop()

        for i in range(1, 10):
            backtrack([i], 1)

        return ans



