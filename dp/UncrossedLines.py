class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m2 = defaultdict(list)
        for i in range(len(nums2)):
            m2[nums2[i]].append(i)
        
        @cache
        def helper(i, curr):
            if curr >= len(nums2) or i >= len(nums1):
                return 0

            found = -1
            if nums1[i] in m2:
                for j in m2[nums1[i]]:
                    if j >= curr:
                        found = j+1
                        break
            if found > -1:
                return max(1+helper(i+1, found), helper(i+1, curr))
            else:
                return helper(i+1, curr)
        
        return helper(0, 0)
      
    def maxUncrossedLinesEditorial(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[n1][n2]
