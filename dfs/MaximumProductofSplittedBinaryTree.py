# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfsTotal(node):
            if not node:
                return 0
            
            node.val += dfsTotal(node.left) + dfsTotal(node.right)
            return node.val
        
        # First pass to calculate the sum of the sub-trees
        total = dfsTotal(root)

        # Second pass to calculate the product after splitting
        stk = [root]
        ans = 0
        while stk:
            n = len(stk)
            for i in range(n):
                node = stk.pop()
                ans = max(ans, (total - node.val) * node.val)
                if node.right:
                    stk.append(node.right)
                if node.left:
                    stk.append(node.left)
        return ans % 1000000007
        

            
            
