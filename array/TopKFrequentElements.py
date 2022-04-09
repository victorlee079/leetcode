from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for c in nums:
            if c not in d:
                d[c] = 0
            d[c] += 1

        sd = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

        ans = []
        for key, val in sd.items():
            ans.append(key)
            k -= 1
            if k == 0:
                break
        return ans

    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        keys = list(count.keys())

        if k >= len(keys):
            return keys
        return nlargest(k, keys, key=count.get)