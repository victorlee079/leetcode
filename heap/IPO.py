class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        pairs = sorted(list(zip(capital, profits)))
        q, i = [], 0
        for _ in range(k):
            while i < n and pairs[i][0] <= w:
                heapq.heappush(q, -pairs[i][1])
                i += 1
            if not q:
                break
            w -= heapq.heappop(q)
        return w
