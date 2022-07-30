class Solution:
    def searchRange(self, nums, target):
        def binarySearchLeft(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x > A[mid]: left = mid + 1
                else: right = mid - 1
            return left

        def binarySearchRight(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x >= A[mid]: left = mid + 1
                else: right = mid - 1
            return right

        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return (left, right) if left <= right else [-1, -1]

    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        
        ridx = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] <= target:
                if nums[mid] == target:
                    ridx = mid
                l = mid + 1
            else:
                r = mid - 1
        
        if ridx == -1:
            return [-1, -1]
        
        l, r = 0, ridx
        lidx = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    lidx = mid
                r = mid - 1
            else:
                l = mid + 1
                
        return [lidx, ridx]
        
        
