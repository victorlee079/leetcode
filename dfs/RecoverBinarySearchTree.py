# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def recoverTree(self, root):                                              
        cur, prev, drops, stack = root, TreeNode(float('-inf')), [], []     
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            if node.val < prev.val:
                drops.append((prev, node))
            prev, cur = node, node.right
        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val
