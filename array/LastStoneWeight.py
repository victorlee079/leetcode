class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones, reverse=True)
            a, b = stones[0], stones[1]
            if a == b:
                stones = stones[2:]
            else:
                stones = stones[2:] + [a-b]
        if len(stones) == 0:
            return 0
        else:
            return stones[-1]
          
    def lastStoneWeightHeap(self, stones: List[int]) -> int:
        stones = [-val for val in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x1 = heapq.heappop(stones)
            x2 = heapq.heappop(stones)
            if x1 != x2:
                heapq.heappush(stones,x1-x2)
        if len(stones) == 0:
            return 0
        return -stones[0]
