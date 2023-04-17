class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        greatest = max(candies)
        ret = [False] * n
        for i in range(n):
            if candies[i] + extraCandies >= greatest:
                ret[i] = True
        return ret
