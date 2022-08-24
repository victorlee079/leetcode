# 1162261467 is the max power of 3 for 32 bits integer
# 3 is a prime number and the only diviors of its  3193^{19}319 are 303^030, 313^131 ... 3193^{19}319
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0
