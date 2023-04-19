# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
            self.ans = 0

            def dfs(node):
                left = right = 0
                if node.left:
                    l, r = dfs(node.left)
                    left = r + 1
                if node.right:
                    l, r = dfs(node.right)
                    right = l + 1
                self.ans = max(self.ans, left, right)
                return left, right
            dfs(root)
            return self.ans
