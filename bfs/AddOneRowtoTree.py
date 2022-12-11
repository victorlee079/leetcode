# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)

        q = deque([root])
        while q:
            n = len(q)
            depth -= 1
            for i in range(n):
                node = q.popleft()
                if depth == 1:
                    left = node.left
                    right = node.right
                    node.left = TreeNode(val, left=left)
                    node.right = TreeNode(val, right=right)
                else:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        return root
