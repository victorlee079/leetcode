"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        q = deque([root])
        while q:
            level = []
            n = len(q)
            for i in range(n):
                node = q.popleft()
                level.append(node.val)
                if node.children:
                    q += node.children
            ans.append(level)
        return ans
