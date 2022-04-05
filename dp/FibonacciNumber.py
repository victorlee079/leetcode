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