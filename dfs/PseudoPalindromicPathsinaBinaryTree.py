# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(hs, node):
            if node.val in hs:
                hs.remove(node.val)
            else:
                hs.add(node.val)      
            
            if not node.left and not node.right:
                if len(hs) <= 1:
                    self.ans += 1
            else:
                if node.left:
                    dfs(hs, node.left)
                if node.right:
                    dfs(hs, node.right)

            if node.val in hs:
                hs.remove(node.val)
            else:
                hs.add(node.val)
        
        dfs(set(), root)
        
        return self.ans
      
    def pseudoPalindromicPathsBit(self, root: TreeNode) -> int:
        count = 0
        
        stack = [(root, 0) ]
        while stack:
            node, path = stack.pop()
            if node is not None:
                # compute occurences of each digit 
                # in the corresponding register
                # Shift 1 to the node.val ith bit
                path = path ^ (1 << node.val)
                # if it's a leaf, check if the path is pseudo-palindromic
                if node.left is None and node.right is None:
                    # check if at most one digit has an odd frequency
                    if path & (path - 1) == 0:
                        count += 1
                else:
                    stack.append((node.right, path))
                    stack.append((node.left, path))
        
        return count
