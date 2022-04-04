class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stk = []
        ans = [0] * n

        for i in range(n):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                j = stk.pop()
                ans[j] = i - j
            stk.append(i)

        return ans