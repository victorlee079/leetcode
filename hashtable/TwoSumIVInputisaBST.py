class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        
        def inorder(node):
            if node.left:
                if inorder(node.left):
                    return True
            if k - node.val in s:
                return True
            s.add(node.val)
            if node.right:
                if inorder(node.right):
                    return True
            return False
        
        return inorder(root)
