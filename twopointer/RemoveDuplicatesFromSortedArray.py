class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = fast = 1
        for i in range(1, len(nums)):
            if nums[slow-1] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow