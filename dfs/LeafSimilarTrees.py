class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(leafs, node):
            if not node.left and not node.right:
                leafs.append(node.val)
                return
            
            if node.left:
                dfs(leafs, node.left)
            if node.right:
                dfs(leafs, node.right)
        
        leafs1 = []
        leafs2 = []
        dfs(leafs1, root1)
        dfs(leafs2, root2)
        return leafs1 == leafs2
