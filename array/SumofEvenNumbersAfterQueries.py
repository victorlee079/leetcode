class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans, even = [], 0
        
        for num in nums:
            if num % 2 == 0:
                even += num
        
        for val, index in queries:
            if nums[index] % 2 == 0:
                even -= nums[index]
            nums[index] += val
            if nums[index] % 2 == 0:
                even += nums[index]
            ans.append(even)
        
        return ans
        
