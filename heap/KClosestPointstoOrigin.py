import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = []
        for p in points:
            d.append((p, (p[0]**2 + p[1]**2) ** (1/2)))
        items = heapq.nsmallest(k, d, key=lambda item: item[1])
        return [items[i][0] for i in range(len(items))]
