# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 0

            left_cnt = dfs(node.left)
            node.left = None if left_cnt == 0 else node.left
            right_cnt = dfs(node.right)
            node.right = None if right_cnt == 0 else node.right

            return node.val + left_cnt + right_cnt

        return root if dfs(root) > 0 else None

    def pruneTreeNoCnt(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None

            node.left = dfs(node.left) 
            node.right = dfs(node.right)
            if not node.left and not node.right:
                return None if node.val == 0 else node
            return node
        
        return dfs(root)
        
