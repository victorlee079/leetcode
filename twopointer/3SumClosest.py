class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        closestSum = sum(nums[:3])
        for i in range(n-2):
            l, r = i+1, n-1
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]
                if currSum == target:
                    return currSum
                elif currSum < target:
                    l += 1
                else:
                    r -= 1
            if abs(target - currSum) < abs(target - closestSum):
                closestSum = currSum
        return closestSum

