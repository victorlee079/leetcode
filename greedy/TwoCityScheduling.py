class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key=lambda x : x[0]-x[1])
        ans, n = 0, len(costs)//2
        for i in range(n):
            ans += costs[i][0]
            ans += costs[n+i][1]
        return ans
