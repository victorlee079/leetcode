# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:        
        if not root:
            return []
        
        ans = []
        def inorder(node):
            if node.left:
                inorder(node.left)
            ans.append(node.val)
            if node.right:
                inorder(node.right)
        inorder(root)
        return ans
      
    def inorderTraversalIter(self, root: Optional[TreeNode]) -> List[int]:        
        if not root:
            return []
        
        ans = []
        node, q = root, []
        while node or q:
            if node:
                q.append(node)
                node = node.left
            else:
                node = q.pop()
                ans.append(node.val)
                node = node.right
        return ans
