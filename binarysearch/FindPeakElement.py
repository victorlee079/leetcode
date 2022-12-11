class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        
        while l <= r:
            mid = l + (r - l) // 2
            if (mid == 0 or nums[mid-1] < nums[mid]) and (mid == n-1 or nums[mid+1] < nums[mid]):
                return mid
            elif (mid == 0 or nums[mid-1] < nums[mid]) and nums[mid] < nums[mid+1]:
                l = mid+1
            else:
                r = mid-1
        return -1
