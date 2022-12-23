class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = [0] * n
        sell = [0] * n
        for i in range(n):
            buy[i] = max(max(sell[:i-1]) - prices[i] if i > 1 else - prices[i], -prices[i])
            sell[i] = max(buy[:i]) + prices[i] if i > 0 else 0
        return max(sell)
    
    def maxProfit0Space(self, prices: List[int]) -> int:
        n = len(prices)
        hold, sell, rest = -inf, 0, 0
        for i in range(n):
            prev = sell
            # Sell if holding
            sell = hold + prices[i]
            # Buy after cooldown or keep hold
            hold = max(hold, rest - prices[i])
            # Keep cooldown or change to cooldown
            rest = max(rest, prev)
        return max(rest, sell)

