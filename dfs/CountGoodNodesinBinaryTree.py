# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = 0
        def dfs(node, best):
            if node.val >= best:
                self.cnt += 1
            best = max(node.val, best)
            if node.left:
                dfs(node.left, best)
            if node.right:
                dfs(node.right, best)
        dfs(root, root.val)
        return self.cnt