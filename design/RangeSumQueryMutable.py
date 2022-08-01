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
            # Last set bit
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

# BITree[0] is a dummy node. 
# BITree[y] is the parent of BITree[x], if and only if y can be obtained by removing the last set bit from the binary representation of x, that is y = x – (x & (-x)).
# The child node BITree[x] of the node BITree[y] stores the sum of the elements between y(inclusive) and x(exclusive): arr[y,…,x). 
