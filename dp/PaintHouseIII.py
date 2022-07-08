class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # dp[i][j][k] minimum cost where we have k neighborhoods in the first i houses and the i-th house is painted with the color j
        dp = [[[0 for k in range(target)] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                for k in range(target):
                    # Init for first house
                    if i == 0:
                        if k > 0:
                            # Not possible k > 0 for first house
                            dp[i][j][k] = math.inf
                            continue
                            
                        if houses[i] == 0:
                            dp[i][j][k] = cost[i][j]
                        else:
                            if houses[i] != j+1:
                                dp[i][j][k] = math.inf                       
                    else:
                        # Not painted
                        if houses[i] == 0:
                            prevCost = dp[i-1][j][k]
                            if k > 0:
                                # Same color with prev and same group, or
                                # different color, different group
                                for l in range(n):
                                    if l == j:
                                        continue
                                    prevCost = min(prevCost, dp[i-1][l][k-1])
                            dp[i][j][k] = prevCost + cost[i][j]
                        else:
                            if j+1 == houses[i]:
                                prevCost = dp[i-1][j][k]
                                if k > 0:
                                    for l in range(n):
                                        if l == j:
                                            continue
                                        prevCost = min(prevCost, dp[i-1][l][k-1])
                                dp[i][j][k] = prevCost
                            else:
                                dp[i][j][k] = math.inf
        
        ans = math.inf
        for i in range(n):
            ans = min(ans, dp[-1][i][-1])
        
        return ans if ans != math.inf else -1
                    
