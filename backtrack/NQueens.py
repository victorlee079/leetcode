class Solution:
    def solveNQueens(self, n):
        ans = []
        
        def pick(path):
            for i in range(n):
                valid = True
                for j, v in enumerate(path):
                    if v == i or abs(i - v) == len(path) - j:
                        valid = False
                    if not valid:
                        break
                if valid:
                    return i
            return None   
        
        def genResult(path):
            ret = []
            for i in path:
                temp = []
                for j in range(n):
                    if i == j:
                        temp.append("Q")
                    else:
                        temp.append(".")
                ret.append("".join(temp))
            return ret

        def backtrack(path, cnt):
            if cnt == 0:
                ans.append(genResult(path))
                return
            
            for i in range(n):
                valid = True
                for j, v in enumerate(path):
                    if v == i or abs(i - v) == len(path) - j:
                        valid = False
                    if not valid:
                        break
                if valid:            
                    path.append(i)
                    backtrack(path, cnt-1)
                    path.pop()
            
        backtrack([], n)
        return ans
