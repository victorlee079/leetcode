class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        a, b = 0, 1
        ans = 0
        for i in range(1, n):
            ans = a + b
            a, b = b, ans
        return ans
    
    # Matrix
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        def multiply(F, M):
            m00 = F[0][0] * M[0][0] + F[0][1] * M[1][0]
            m01 = F[0][0] * M[0][1] + F[0][1] * M[1][1]
            m10 = F[1][0] * M[0][0] + F[1][1] * M[0][1]
            m11 = F[1][0] * M[0][1] + F[1][1] * M[1][1]
            F[0][0], F[0][1], F[1][0], F[1][1] = m00, m01, m10, m11
            
        F = [[1, 1], [1, 0]]
        M = [[1, 1], [1, 0]]
    
        def power(F, n):
            if n <= 1:
                return
            
            power(F, n // 2)
            multiply(F, F)
            if n % 2 != 0:
                multiply(F, M)
        
        power(F, n-1)
        return F[0][0]
