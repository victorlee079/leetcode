# Find the depth of leftmost node
def depth(node):
    d = 0
    while node:
        d += 1
        node = node.left
    return d

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0

        l = depth(root.left)
        r = depth(root.right)
        
'''
Case 1:
1
| \
2   3
| \ |
4 5 6

Left side is completely filled. 
(2 ** l - 1) + 1
Nodes in left + root

Case 2:
1
| \
2  3
| \
4 5

Right side is completely filled.

'''
        
        # Equal means the left side is complete completely filled
        if l == r:
            return 2 ** l + self.countNodes(root.right)
        # left side must be larger than right side, this means right side is completely filled
        else:
            return 2 ** r + self.countNodes(root.left)
        
