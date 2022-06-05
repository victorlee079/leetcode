class Solution:
    def totalNQueens(self, n: int) -> int:
        self.cnt = 0

        def isValid(path, i):
            r = len(path)
            for j in range(r):
                if path[j] == i or abs(i - path[j]) == r - j:
                    return False
            return True

        def backtrack(path):
            if len(path) == n:
                self.cnt += 1
                return

            for i in range(n):
                if isValid(path, i):
                    path.append(i)
                    backtrack(path)
                    path.pop()
            return

        backtrack([])
        return self.cnt