class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r, n = max(weights), sum(weights), len(weights)

        def canShip(capacity):
            day, weight, index = 0, 0, 0
            while day < days:
                while index < n:
                    if weight + weights[index] <= capacity:
                        weight += weights[index]
                    else:
                        break
                    index += 1
                if index == n:
                    return True
                day += 1
                weight = 0
            return False

        while l < r:
            m = l + (r - l) // 2
            if canShip(m):
                r = m
            else:
                l = m + 1
        return l
