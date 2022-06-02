class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = cur = total = 0
        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            if cur < 0:
                cur = 0
                start = i+1
            total += gas[i] - cost[i]
        if total < 0:
            return -1
        return start
