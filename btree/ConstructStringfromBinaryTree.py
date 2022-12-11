# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = []
        def preorder(node):
            ans.append(str(node.val))
            if node.left:
                ans.append("(")
                preorder(node.left)
                ans.append(")")
            if node.right:
                if not node.left:
                    ans.append("()")
                ans.append("(")
                preorder(node.right)
                ans.append(")")
        preorder(root)
        return "".join(ans)
            
