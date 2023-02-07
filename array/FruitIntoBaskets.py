class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        baskets = {}
        ans = 0
        for r in range(len(fruits)):
            fruit = fruits[r]
            if fruit in baskets:
                baskets[fruit] += 1
            else:
                baskets[fruit] = 1
                while len(baskets) > 2:
                    prev = fruits[l]
                    baskets[prev] -= 1
                    if baskets[prev] == 0:
                        del baskets[prev]
                    l += 1
            ans = max(ans, sum(baskets.values()))
        return ans
