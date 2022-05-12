# O(N!) for unique 
# O(N!/(N-K)!) for duplicate
def backtrack(ret, nums, path):
    if len(nums) == 0:
        ret.append(path[::])
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        path.append(nums[i])
        backtrack(ret, nums[:i] + nums[i+1:], path)
        path.pop()
        

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        backtrack(ret, nums, [])
        return ret

        
