# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # build a tree -> Normally using recursion
    # Preorder -> Root go first
    # Inorder -> Contains number of elements in the left and in the right
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root = preorder[0]
        ileft = inorder[:inorder.index(root)]
        iright = inorder[inorder.index(root)+1:]
        pleft = preorder[1:1+len(ileft)]
        pright = preorder[1+len(pleft):]
        
        return TreeNode(val=root, left=self.buildTree(pleft, ileft), right=self.buildTree(pright, iright))
