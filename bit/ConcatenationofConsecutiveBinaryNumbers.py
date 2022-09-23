class Solution:
    def concatenatedBinary(self, n: int) -> int:
        if n == 1:
            return 1
        return ((self.concatenatedBinary(n-1) << (len(bin(n))-2)) + n) % 1000000007
