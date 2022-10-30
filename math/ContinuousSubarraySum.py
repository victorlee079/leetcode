class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = defaultdict(int)
      
        curr = 0
        for i in range(len(nums)):
            # (a + n * k) % k = a
            curr += nums[i]
            curr %= k
            
            # running sum == 0 and current index >= 1 (i.e. at least 2 consecutive elements)
            if curr == 0 and i > 0:
                return True
            if curr in d and i - d[curr] >= 2:
                return True
            if curr not in d:
                d[curr] = i

        return False
