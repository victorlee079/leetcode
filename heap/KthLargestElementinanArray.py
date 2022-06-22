class Solution:
    # O(k + (n-k) log k)
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

    # O(n) in average
    def findKthLargestQs(self, nums, k):
        def partition(nums, start, end):
            
            # Random select the pivot
            pivot_index = random.randint(start, end)
            
            # Put to the end
            nums[end], nums[pivot_index] = nums[pivot_index], nums[end]
            
            ptr = start
            for i in range(start, end):
                if nums[i] < nums[end]:
                    # Smaller than the pivot, put to the left
                    nums[ptr], nums[i] = nums[i], nums[ptr]
                    ptr += 1
            
            # Put the pivot to the final position
            nums[end], nums[ptr] = nums[ptr], nums[end]
            return ptr
            
            
        def quickselect(nums, start, end, k):
            if start <= end:
                pos = partition(nums, start, end)
                if pos > k:
                    return quickselect(nums, start, pos-1, k)
                elif pos < k:
                    return quickselect(nums, pos+1, end, k)
                else:
                    return nums[pos]
        
        return quickselect(nums, 0, len(nums)-1, len(nums)-k)
