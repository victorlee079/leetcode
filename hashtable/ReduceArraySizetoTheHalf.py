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
        
    def minSetSizeBuckets(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        s = n
        # O(n)
        counts = Counter(arr)
        
        buckets = [0] * (n+1)
        for item in counts.items():
            buckets[item[1]] += 1
        
        for i in range(n, 0, -1):
            for j in range(buckets[i]):
                s -= i
                ans += 1
                if s <= n//2:
                    return ans

        return ans
        
