class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        ans = s = 0
        # O(n)
        counts = Counter(arr)
        # O(n log n)
        items = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        for item in items:
            ans += 1
            s += item[1]
            if s >= n // 2:
                return ans
        return len(ans)
        
