# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cnt = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node):
            if not node:
                return None

            if node.left:
                res = dfs(node.left)
                if res is not None:
                    return res

            self.cnt += 1
            if self.cnt == k:
                return node.val

            if node.right:
                res = dfs(node.right)
                if res is not None:
                    return res

        return dfs(root)