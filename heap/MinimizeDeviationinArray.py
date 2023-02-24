class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        q = []
        ans = low = inf
        for num in nums:
            if num % 2 == 1:
                num *= 2
            heapq.heappush(q, -num)
            low = min(low, num)
        while q[0] % 2 == 0:
            val = -heapq.heappop(q)
            ans = min(ans, val-low)
            val //= 2
            low = min(low, val)
            heapq.heappush(q, -val)
        return min(ans, -q[0]-low)
