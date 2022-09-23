class Solution:
    def concatenatedBinaryRecur(self, n: int) -> int:
        if n == 1:
            return 1
        return ((self.concatenatedBinary(n-1) << (len(bin(n))-2)) + n) % 1000000007
    
    def concatenatedBinaryIter(self, n: int) -> int:
        ans = 1
        for i in range(2, n+1):
            ans = ((ans << (len(bin(i))-2)) + i) % 1000000007
        return ans
