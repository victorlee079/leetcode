class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        ans, min_heap = 0, []
        # O(k + n log k)
        for pile in piles:
            if len(min_heap) < k:
                heapq.heappush(min_heap, pile)
            else:
                # Remaining items: k < len(piles)
                ans += heapq.heappushpop(min_heap, pile)

        n = len(min_heap)

        # Convert to max_heap to pop the largest
        # O(k log k)
        max_heap = []
        for p in min_heap:
            heapq.heappush(max_heap, -p)

        # Apply k operations to each element
        # O(k log k)
        for _ in range(k):
            p = -heapq.heappop(max_heap)
            p = p - p // 2
            # Push back for k > len(piles)
            heapq.heappush(max_heap, -p)

        # negative for max heap in python
        return ans - sum(max_heap)
        
    def minStoneSumJustMaxHeap(self, piles: List[int], k: int) -> int:
        piles = [-p for p in piles]
        heapq.heapify(piles)
        for _ in range(k):
            curr = -piles[0]
            heapq.heapreplace(piles, -(curr - curr // 2))
        return -sum(piles)
