# O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        d = defaultdict(int)
        res = [-1] * n
        
        for i in range(n):
            num = nums[i]
            if -1000000000 <= num <= 1000000000:
                d[num] = i
            
        def count(i):
            # Not visited
            if res[i] == -1:
                num = nums[i]
                if num-1 in d:
                    ret = 1 + count(d[num-1])
                    res[i] = ret
                else:
                    res[i] = 1
            return res[i]
        
        ans = 0
        for i in range(n):
            ans = max(ans, count(i))
        return ans
      
    def longestConsecutiveSol(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            # Only compute the smallest
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
