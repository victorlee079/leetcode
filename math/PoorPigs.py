class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        n = minutesToTest // minutesToDie
        return math.ceil(math.log(buckets, n+1)) # log a / log b = logb a
