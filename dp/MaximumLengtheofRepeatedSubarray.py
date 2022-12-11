class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [[0] * n2 for _ in range(n1)]
        for i in range(n1):
            for j in range(n2):
                if nums1[i] == nums2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
        # More efficient than setting max for each cell becoz max() is written in C program
        return max(max(row) for row in dp)
        
