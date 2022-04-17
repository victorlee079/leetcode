from collections import Counter

class Solution:
    def numOfPairs(self, nums, target):
        n = len(nums)
        ans = 0
        d = Counter(nums)
        for i, v in d.items():
            if target[:len(i)] == i:
                if i + i == target:
                    ans += v * (v-1)
                else:
                    ans += v * d[target[len(i):]]
            
        return ans
