class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(path, index, nums):
            if len(path) >= 2:
                ans.append(path[::])

            seen = set()
            for i in range(index, len(nums)):
                if i > index and nums[i] in seen:
                    continue
                if not path or nums[i] >= path[-1]:
                    path.append(nums[i])
                    seen.add(nums[i])
                    backtrack(path, i+1, nums)
                    path.pop()
        backtrack([], 0, nums)
        return ans
