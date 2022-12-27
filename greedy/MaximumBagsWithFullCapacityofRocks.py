class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        ans = 0
        rems = []

        for i in range(n):
            rem = capacity[i] - rocks[i]
            if rem == 0:
                ans += 1
            else:
                rems.append(rem)

        rems = sorted(rems)

        for i in range(len(rems)):
            if additionalRocks >= rems[i]:
                ans += 1
                additionalRocks -= rems[i]
            else:
                break
        return ans
