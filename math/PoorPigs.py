class Solution:
    def poorPigsLog(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        n = minutesToTest // minutesToDie
        return math.ceil(math.log(buckets, n+1)) # log a / log b = logb a
    
    # e.g. 60 mins test and 15 mins die, 0, 15, 30, 45, 60 ==> 5 trials
    # i.e. buckets can be tested in 5 rounds
    # Number of pigs are the dimension to create
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        pigs = 2 # base case
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs
