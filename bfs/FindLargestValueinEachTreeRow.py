# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []

        def bfs(q):
            if not q:
                return

            largest = -math.inf
            nq = []
            while q:
                node = q.pop()
                if node.val > largest:
                    largest = node.val
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            ans.append(largest)
            bfs(nq)

        bfs([root])

        return ans