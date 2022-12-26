class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums = sorted(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
        
        def search(val):
            l, r = 0, n
            while l < r:
                mid = l + (r - l) // 2
                # bisect_right
                if nums[mid] <= val:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        ans = [0] * len(queries)
        for i in range(len(queries)):
            ans[i] = search(queries[i])
        return ans
            