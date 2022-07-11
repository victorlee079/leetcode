class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) + 1
        cost = cost + [0]
        for i in range(2, n):
            cost[i] += min(cost[i-1], cost[i-2])
        return cost[-1]
