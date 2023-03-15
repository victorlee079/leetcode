# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = deque([(root, 0)])
        while q:
            size = len(q)
            for i in range(size):
                node, curr = q.popleft()
                curr = curr * 10 + node.val
                if not node.left and not node.right:
                    ans += curr
                if node.left:
                    q.append((node.left, curr))
                if node.right:
                    q.append((node.right, curr))
        return ans
