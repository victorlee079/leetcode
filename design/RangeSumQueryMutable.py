class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.bitree = [0] * (self.n+1)
        self.nums = nums
        self.isInit = False
        for i in range(self.n):
            self.update(i, nums[i])
        self.isInit = True

    def update(self, index: int, val: int) -> None:
        diff = val
        if self.isInit:
            diff = val - self.nums[index]
            self.nums[index] = val
        i = index + 1        
        while i <= self.n:
            self.bitree[i] += diff
            i += i & (-i)

    def sumRange(self, left: int, right: int) -> int:
        def getSum(i):
            s = 0
            i += 1
            while i > 0:
                s += self.bitree[i]
                i -= i & (-i)
            return s

        return getSum(right) - getSum(left-1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
