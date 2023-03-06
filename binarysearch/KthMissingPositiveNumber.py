class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        l, r = 0, n-1
        while l <= r:
            m = l + (r - l) // 2
            if arr[m] - (m+1) < k:
                l = m + 1
            else:
                r = m - 1
        return l + k
