class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = set([0, 1, 2, 5, 6, 8, 9])
        ng = set([0, 1, 8])
        ret = 0
        for i in range(n+1):
            s = set([int(j) for j in str(i)])
            if s.issubset(valid) and not s.issubset(ng):
                ret += 1
        return ret
    
    def rotatedDigits2(self, N: int) -> int:
        count = 0
        for d in range(1, N+1):
            # O(log n)
            d = str(d)
            if '3' in d or '4' in d or '7' in d:
                continue
            if '2' in d or '5' in d or '6' in d or '9' in d:
                count+=1
        return count
