class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        ans = 0
        for i in range(len(costs)):
            if coins < costs[i]:
                break
            coins -= costs[i]
            ans += 1
        return ans
