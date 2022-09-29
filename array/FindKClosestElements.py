class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for num in arr:
            if len(heap) < k:
                heapq.heappush(heap, (-abs(num-x), num))
            else:
                diff = -heap[0][0]
                if abs(num-x) < diff:
                    heapq.heappushpop(heap, (-abs(num-x), num))
        return sorted([item[1] for item in heap])
                
