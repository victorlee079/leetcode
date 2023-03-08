class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def canEat(k):
            times = 0
            for i in range(len(piles)):
                # Ceiling division
                times += (piles[i] - 1) // k + 1
            return times <= h

        while l <= r:
            m = l + (r - l) // 2
            if canEat(m):
                r = m - 1
            else:
                l = m + 1
        return l
