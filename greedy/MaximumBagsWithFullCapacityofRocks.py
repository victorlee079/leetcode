class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        ans = 0

        for i in range(n):
            capacity[i] -= rocks[i]

        capacity = sorted(capacity)

        for i in range(n):
            if additionalRocks >= capacity[i]:
                ans += 1
                additionalRocks -= capacity[i]
            else:
                break
        return ans