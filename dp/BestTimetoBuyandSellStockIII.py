'''
dp[k, i] = max(dp[k, i-1], max(prices[i] - prices[j] + dp[k-1, j-1]) for j=[0..i])
    when i == j, waste a transaction
dp[k, i-1] ==> Don't trade
prices[i] - prices[j] + dp[k-1, j-1] ==> Profit for i - j and max profit last transaction at j
'''

'''
        public int MaxProfitDp(int[] prices) {
            if (prices.Length == 0) return 0;
            var dp = new int[3, prices.Length];
            for (int k = 1; k <= 2; k++)  {
                for (int i = 1; i < prices.Length; i++) {
                    // Repeat every time 
                    int min = prices[0]; 
                    for (int j = 1; j <= i; j++)
                        min = Math.Min(min, prices[j] - dp[k-1, j-1]);
                    // Repeat every time
                    dp[k, i] = Math.Max(dp[k, i-1], prices[i] - min);
                }
            }

            return dp[2, prices.Length - 1];
        }
'''

# Time complexity is O(kn), space complexity is O(kn).
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * n for _ in range(2)]

        for k in range(2):
            min_price = prices[0]
            for i in range(1, n):
                min_price = min(min_price, prices[i] - dp[k - 1][i - 1])
                dp[k][i] = max(prices[i] - min_price, dp[k][i - 1])

        return dp[1][-1]