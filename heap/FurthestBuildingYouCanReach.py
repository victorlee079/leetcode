class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                # Use a ladder first
                heapq.heappush(heap, diff)
            if len(heap) > ladders:
                # Replace the smallest jump by brick
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                # Cannot make this move
                return i
        return len(heights)-1
