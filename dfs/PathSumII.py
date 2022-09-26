# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        
        def dfs(path, node, s):
            if not node:
                return
            
            path.append(node.val)
            s += node.val
            if not node.left and not node.right and s == targetSum:
                ans.append(path[::])
                
            if node.left:
                dfs(path, node.left, s)
            if node.right:
                dfs(path, node.right, s)
            path.pop()
        
        dfs([], root, 0)
        
        return ans
            
