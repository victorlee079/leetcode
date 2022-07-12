class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        
        target = sum(nums) // k
        
        sums = [0] * k
        
        nums.sort(reverse=True)
        
        def backtrack(index):
            if index == len(nums):
                return True
        
            for j in range(k):
                if sums[j] + nums[index] <= target:
                    sums[j] += nums[index]
                    if backtrack(index+1):
                        return True
                    sums[j] -= nums[index]
                    # Algo always fill previous buckets
                    # for k > p > j, sums[p] is also zero which make no differences
                    if sums[j] == 0:
                        break
            return False                    
            
        return backtrack(0)
            
