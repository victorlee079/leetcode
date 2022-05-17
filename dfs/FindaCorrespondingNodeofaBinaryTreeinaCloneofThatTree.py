# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(path, node, target):
            if node == target:
                return path
            
            if node:
                
                if node.left:
                    path.append("L")
                    ret = dfs(path, node.left, target)
                    if ret:
                        return ret
                    path.pop()
                    
                if node.right:
                    path.append("R")
                    ret = dfs(path, node.right, target)
                    if ret:
                        return ret
                    path.pop()
                    
            return None
        
        path = dfs([], original, target)
        
        for i in range(len(path)):
            direction = path[i]
            if direction == "L":
                cloned = cloned.left
            elif direction == "R":
                cloned = cloned.right
        return cloned
