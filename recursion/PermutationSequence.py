import math


class Solution:
    def getPermutation(self, n, k):
        avails = [str(i+1) for i in range(n)]

        def permutate(nums, k, path):
            if len(nums) == 1:
                return "".join(path + nums)

            index = k // math.factorial(len(nums)-1)
            rem = k % math.factorial(len(nums)-1)
            path.append(nums[index])
            return permutate(nums[:index] + nums[index+1:], rem, path)

        return permutate(avails, k-1, [])

s = Solution()
for i in range(6):
    print(s.getPermutation(3, i+1))
