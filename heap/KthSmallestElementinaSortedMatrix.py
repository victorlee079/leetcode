class Solution:
    # Time: O(k) + O((n-k) log k)
    # Space: O(k)
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        
        m, n = len(matrix), len(matrix[0])
        for r in range(m):
            for c in range(n):
                if len(heap) < k:
                    heapq.heappush(heap, -matrix[r][c])
                else:
                    if matrix[r][c] < -heap[0]:
                        heapq.heappushpop(heap, -matrix[r][c])
        return -heap[0]
