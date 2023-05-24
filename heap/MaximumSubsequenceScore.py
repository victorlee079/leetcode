class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        pairs = zip(nums1, nums2)
        pairs = sorted(pairs, key=lambda p: -p[1])
        
        heap = []
        curr = 0
        for a, b in pairs:
            if len(heap) < k:
                curr += a
                heapq.heappush(heap, (a, b))
            else:
                c, d = heapq.heappushpop(heap, (a, b))
                curr = curr - c + a
            if len(heap) == k:
                ans = max(ans, curr * b)
        return ans
