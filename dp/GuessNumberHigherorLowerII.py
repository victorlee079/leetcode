class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(n+1)]

        def compute(dp, start, end):
            if start >= end:
                return 0
            if dp[start][end]:
                return dp[start][end]
            
            ret = math.inf
            for i in range(start, end+1):
                # Guess i incorrectly
                # minimum maximum cost to 
                ret = min(ret, max(compute(dp, start, i-1), compute(dp, i+1, end)) + i)
            dp[start][end] = ret
            return ret
        
        return compute(dp, 1, n)
    
'''
    we are given lower bound and upper bound of the range, and the target is unknown
    for each guess, it can be:
        hit the target
        smaller than target
        higher than target
        if not hit
        we pay the amount of guess number and continue the next guess
        we are told whether higher of lower, which means we can narrow down the lower/upper bound
    for each guess
        the money we pay is based on the status of previous one, total money needed and the boundary
        so think about using dp to store the previous statuses
    what status / value we need to track?
        the money we need if the bound is [lo hi]
    define dp[n+1][n+1]
    dp[i][j] represents the money we need if the lo = i and hi = j
    based case
        if i >= j, then we hit the target and no need to pay, so return 0
        if dpi][j] != 0, we have calculated the money we need to pay, return the value
    transition function
        i = [lo hi]
        i is the number we guess
        i divides the array into [lo, i) and (i, hi]
        the target can be in either part, to make sure we have ENOUGH money for the next guess, get max between them
        get the min between the current and the maximum of left and right part
'''
