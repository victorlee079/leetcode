class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        skylines = []
        for left, right, height in buildings:
            skylines.append((left, -height, right))
            skylines.append((right, 0, 0))

        result = [[0, 0]]
        heap = [(0, float('inf'))]
        for left, nheight, right in sorted(skylines):
            while left >= heap[0][1]:
                heapq.heappop(heap)
            if nheight:
                heapq.heappush(heap, (nheight, right))
            height = -heap[0][0]
            if result[-1][1] != height:
                result.append([left, height])
        return result[1:]
