# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(path, node):
            if not node:
                return
            
            path.append(node)
            if node.left:
                dfs(path, node.left)
            if node.right:
                dfs(path, node.right)
            
        q = deque()
        dfs(q, root)
        
        if q:
            curr = q.popleft()            
            while q:
                node = q.popleft()
                curr.left, curr.right = None, node
                curr = node
            
        return root
