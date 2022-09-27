class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        left = [0] * n
        right = [0] * n
        
        for i in range(n):
            if dominoes[i] == "R":
                right[i] = n
            elif dominoes[i] == "L":
                right[i] = 0
            else:
                right[i] = right[i-1] - 1 if i > 0 and right[i-1] > 0 else 0
                
        for i in range(n-1, -1, -1):
            if dominoes[i] == "R":
                left[i] = 0
            elif dominoes[i] == "L":
                left[i] = n
            else:
                left[i] = left[i+1] - 1 if i < n-1 and left[i+1] > 0 else 0
            
        ans = []
        for i in range(n):
            f = right[i] - left[i]
            if f > 0:
                ans.append("R")
            elif f < 0:
                ans.append("L")
            else:
                ans.append(".")
        
        return "".join(ans)
            
