# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(node, low, high):
            if not node:
                return high - low
            
            low = min(node.val, low)
            high = max(node.val, high)
            left = dfs(node.left, low, high)
            right = dfs(node.right, low, high)
            return max(left, right)
            
        return dfs(root, root.val, root.val)
