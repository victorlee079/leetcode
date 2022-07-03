class Solution:
    # O(n^2)
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        # Longest wiggle sequence with last one is increasing
        up = [0] * n
        # Longest wiggle sequence with last one is decreasing
        down = [0] * n
        for i in range(1, n):
            for j in range(i):
                # Construct the sequence by skipping the middles
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j] + 1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j] + 1)
                # Ignore same value
        return 1 + max(up[n - 1], down[n - 1])

    # Time O(n)
    # Space O(1)
    def wiggleMaxLengthLinear(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        up = down = 1
        for i in range(1, n):
            for j in range(i):
                # Construct the sequence by skipping the middles
                if nums[i] > nums[j]:
                    up = down + 1
                elif nums[i] < nums[j]:
                    down = up + 1
        return max(up[n-1], down[n-1])

    # Number of alternating max and min peaks
    def wiggleMaxLengthGreedy(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        # indicate uptrend or downtrend
        prev = nums[1] - nums[0]
        ans = 2 if prev != 0 else 1
        for i in range(2, n):
            diff = nums[i] - nums[i-1]
            if (diff > 0 and prev <= 0) or (diff < 0 and prev >= 0):
                ans += 1
                prev = diff
        return ans