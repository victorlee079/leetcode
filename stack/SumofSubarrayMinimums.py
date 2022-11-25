class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = pow(10, 9) + 7
        ret, stk = 0, []
        
        for i in range(len(arr)):
            val = arr[i]
            # Increasing monotonic stack (current value is the recent smallest)
            # e.g. [3, 4, 2] and 2 is the smallest
            # Tuple in stk: (value, index+1, mins)
            while stk and stk[-1][0] > val:
                stk.pop()

            curr, index = val, i+1
            pi, pm = 0, 0
            if stk and stk[-1]:
                prev, pi, pm = stk[-1]
            mem = curr * (index - pi) + pm
            # ret != mem as it contains mins from popped out
            ret += mem
            stk.append((val, i+1, mem))
            ret %= MOD
        return ret
