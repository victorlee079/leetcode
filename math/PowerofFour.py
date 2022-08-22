class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        return (math.log(n, 4)).is_integer()

    def isPowerOfFour(self, n: int) -> bool:
        return n >= 1 and n & (n-1) == 0 and 0b1010101010101010101010101010101 & n == n 
