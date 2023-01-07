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

    def canCompleteCircuit20230107(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        cum, total, ans = 0, 0, -1
        for i in range(n):
            diff = gas[i] - cost[i]
            cum += diff
            if cum < 0:
                ans = -1
                cum = 0
            else:
                if ans == -1:
                    ans = i
            total += diff
        return ans if total > -1 else -1
