class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        running_sum = count = 0
        d = {0: 1}
        for i in range(len(nums)):
            running_sum += nums[i]
            rem = running_sum % k
            if rem in d:
                count += d[rem]
                d[rem] += 1
            else:
                d[rem] = 1
        return count
