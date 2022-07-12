class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        
        target = sum(nums) // k
        
        sums = [target] * k
        
        nums.sort(reverse=True)
        
        def backtrack(index):
            if index == len(nums):
                return True
        
            for j in range(k):
                if sums[j] >= nums[index]:
                    sums[j] -= nums[index]
                    if backtrack(index+1):
                        return True
                    sums[j] += nums[index]
                    if nums[index] == sums[j]:
                        break
            return False                    
            
        return backtrack(0)
            
