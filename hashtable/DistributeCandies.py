class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        hm = {}
        cnt = len(candyType) // 2
        for candy in candyType:
            if candy not in hm:
                hm[candy] = 0
            hm[candy] += 1
            if len(hm.items()) >= cnt:
                return cnt
        return len(hm.items())