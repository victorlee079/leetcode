class Solution:
    def countOdds(self, low: int, high: int) -> int:

        count = high - low + 1
        if count % 2 == 0:
            return count // 2
        else:
            if high % 2 == 0:
                return count // 2
            else:
                return count // 2 + 1
