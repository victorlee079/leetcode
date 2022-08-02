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

    # Time: O(n^2)
    # Space: O(1)
    def kthSmallestBinarySearch(self, matrix: List[List[int]], k: int) -> int:
        n, lo, hi = len(matrix), matrix[0][0], matrix[-1][-1]
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            cnt = 0
            ans = lo
            
            for r in range(n):
                for c in range(n):
                    if matrix[r][c] > mid:
                        break
                    else:
                        cnt += 1
                        ans = max(ans, matrix[r][c])
            
            if cnt == k:
                return ans
            
            if cnt > k:
                hi = mid - 1
            else:
                lo = mid + 1
                
        return lo
                
            
                        
