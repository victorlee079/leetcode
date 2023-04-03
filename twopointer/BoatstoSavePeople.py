class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people = sorted(people)
        l, r = 0, n-1
        ans = 0
        while l <= r:
            while l < r and people[l] + people[r] > limit:
                ans += 1
                r -= 1
            ans += 1
            l += 1
            r -= 1
        return ans
