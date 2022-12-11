class Solution:   
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def dfs(currSum, node):
            currSum += node.val
            if not node.left and not node.right:
                if currSum == targetSum:
                    return True
            
            return (node.left and dfs(currSum, node.left)) or (node.right and dfs(currSum, node.right))
            
        return dfs(0, root)