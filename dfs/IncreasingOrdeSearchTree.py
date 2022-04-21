# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stk = []

        def dfs(node):
            if not node:
                return None

            if node.left:
                dfs(node.left)
            stk.append(node)
            if node.right:
                dfs(node.right)

        dfs(root)
        curr = None
        while stk:
            node = stk.pop()
            node.left = None
            if curr:
                node.right = curr
            curr = node
        return curr
