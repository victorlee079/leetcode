class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest, profit = inf, 0
        for price in prices:
            lowest = min(lowest, price)
            profit = max(profit, price - lowest)
        return profit
