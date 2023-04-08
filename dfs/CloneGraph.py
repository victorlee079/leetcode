"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        d = {}

        def dfs(n):
            if n.val in d:
                return d[n.val]

            nn = Node(n.val, None)
            d[n.val] = nn
            if n.neighbors:
                nn.neighbors = []
            for i in n.neighbors:
                nn.neighbors.append(dfs(i))
            return nn

        head = dfs(node)
        return head
