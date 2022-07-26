# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, path, target):
            if root == target:
                return True
            
            if root.left:
                path.append(root.left)
                if dfs(root.left, path, target):
                    return True
                path.pop()
            if root.right:
                path.append(root.right)
                if dfs(root.right, path, target):
                    return True
                path.pop()
            return False
        
        path = [root]
        dfs(root, path, p)
        for n in range(len(path)-1, -1, -1):
            common = [path[n]]
            if dfs(path[n], common, q):
                return path[n]
        return None

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(stk, target):
            if stk[-1] == target:
                return True
            
            node = stk[-1]
            if node.left:
                stk.append(node.left)
                if dfs(stk, target):
                    return True
                stk.pop()
            if node.right:
                stk.append(node.right)
                if dfs(stk, target):
                    return True
                stk.pop()
            
            return False
                
        stk = [root]
        dfs(stk, p)
        while stk:
            node = stk[-1]
            if dfs([node], q):
                return node
            stk.pop()
        return None
