# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [(root, 0)]
        
        def bfs(width, q):            
            if not q:
                return width
            
            start, end, nq = -1, -1, []
            while q:
                (node, index) = q.pop(0)
                if start < 0:
                    start = end = index
                else:
                    end = index
                if node.left:
                    nq.append((node.left, 2*index))
                if node.right:
                    nq.append((node.right, 2*index+1))
            return bfs(max(width, end-start+1), nq)
        return bfs(0, q)
