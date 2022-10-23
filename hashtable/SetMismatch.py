class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * n
        for num in nums:
            arr[num-1] += 1
        twice = None
        missing = None
        for i in range(n):
            if arr[i] > 1:
                twice = i+1
            if arr[i] == 0:
                missing = i+1
            if twice and missing:
                break
        return [twice, missing]

    def findErrorNumsMath(self, nums: List[int]) -> List[int]:
        n, a, b = len(nums), sum(nums), sum(set(nums))
        s = n * (n+1) // 2
        return [a-b, s-b]
