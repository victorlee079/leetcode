class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        n, m = len(spells), len(potions)
        potions = sorted(potions)
        for i in range(n):
            spell = spells[i]
            left, right = 0, m
            while left < right:
                mid = left + (right - left) // 2
                if spell * potions[mid] < success:
                    left = mid + 1
                else:
                    right = mid
            ans.append(m - left)
        return ans
