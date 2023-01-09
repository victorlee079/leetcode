# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def preorder(node):
            if not node:
                return
            ans.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ans

    def preorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        q = [root]
        ans = []
        while q:
            node = q.pop(-1)
            if not node:
                break
            ans.append(node.val)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return ans
