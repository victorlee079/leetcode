# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from sortedcontainers import SortedList


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(SortedList)
        self.minc = self.maxc = 0
        self.minr = self.maxr = 0

        def dfs(node, r, c):
            if node:
                self.minc = min(self.minc, c)
                self.maxc = max(self.maxc, c)
                self.minr = min(self.minr, r)
                self.maxr = max(self.maxr, r)
                d[(r, c)].add(node.val)
                if node.left:
                    dfs(node.left, r + 1, c - 1)
                if node.right:
                    dfs(node.right, r + 1, c + 1)

        dfs(root, 0, 0)

        ans = []
        for i in range(self.minc, self.maxc + 1):
            temp = []
            for j in range(self.minr, self.maxr + 1):
                if (j, i) in d:
                    temp.extend(d[(j, i)])

            if temp:
                ans.append(temp)

        return ans

    def verticalTraversalOptimized(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        self.minc = self.maxc = 0

        def dfs(node, r, c):
            if node:
                self.minc = min(self.minc, c)
                self.maxc = max(self.maxc, c)
                d[c].append((r, node.val))
                dfs(node.left, r + 1, c - 1)
                dfs(node.right, r + 1, c + 1)

        dfs(root, 0, 0)

        ans = []
        for i in range(self.minc, self.maxc + 1):
            # Sorting order: item[0], item[1]
            ans.append([item[1] for item in sorted(d[i])])

        return ans
