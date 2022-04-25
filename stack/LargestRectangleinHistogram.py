class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        ls, rs = [0] * n, [0] * n
        left_stk, right_stk = [], []
        # Monotonic Stack - Find the next right item that smaller than itself
        for i in range(n - 1, -1, -1):
            while right_stk and heights[right_stk[-1]] >= heights[i]:
                right_stk.pop()
            rs[i] = n if not right_stk else right_stk[-1]
            right_stk.append(i)
        # Monotonic Stack - Find the next left item that smaller than itself
        for i in range(n):
            while left_stk and heights[left_stk[-1]] >= heights[i]:
                left_stk.pop()
            ls[i] = -1 if not left_stk else left_stk[-1]
            left_stk.append(i)

        largest = 0
        for i in range(n):
            largest = max(largest, heights[i] * (rs[i] - ls[i] - 1))
        return largest

    def largestRectangleArea2(self, heights):
        stack, ans = [], 0
        for i, h in enumerate(heights + [0]):
            # Next right smaller is found
            # Increasing stack
            while stack and heights[stack[-1]] >= h:
                # left smaller
                H = heights[stack.pop()]
                W = i if not stack else i-stack[-1]-1
                ans = max(ans, H*W)
            stack.append(i)
        return ans
