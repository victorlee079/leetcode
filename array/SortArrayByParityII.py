class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        e, o = 0, 1

        while e < len(nums) and o < len(nums):
            if nums[e] % 2 == 0:
                e += 2
            elif nums[o] % 2 == 1:
                o += 2
            else:
                nums[o], nums[e] = nums[e], nums[o]
        return nums