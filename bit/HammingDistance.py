class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        tmp = x ^ y
        cnt = 0
        while tmp > 0:
            cnt += tmp % 2
            tmp = tmp >> 1
        return cnt
