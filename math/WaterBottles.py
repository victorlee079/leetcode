class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        ans = 0
        empty = 0
        while numBottles > 0:
            ans += numBottles
            numBottles, empty = (empty + numBottles) // numExchange, (numBottles + empty) % numExchange
        return ans