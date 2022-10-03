class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        dp = [None] * n
        dp[0] = (0, neededTime[0])

        for i in range(1, n):
            if colors[i] == colors[i-1]:
                if neededTime[i] <= dp[i-1][1]:
                    dp[i] = (dp[i-1][0] + neededTime[i], dp[i-1][1])
                else:
                    dp[i] = (dp[i-1][0] + dp[i-1][1], neededTime[i])
            else:
                dp[i] = (dp[i-1][0], neededTime[i])
        
        return dp[-1][0]

    def minCostSpaceOpt(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        res, maxTime = 0, neededTime[0]

        for i in range(1, n):
            if colors[i] == colors[i-1]:
                if neededTime[i] <= maxTime:
                    res += neededTime[i]
                else:
                    res += maxTime
                    maxTime = neededTime[i]
            else:
                maxTime = neededTime[i]    
        
        return res
                
            
