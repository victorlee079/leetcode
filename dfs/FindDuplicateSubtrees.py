class Solution:
    def findDuplicateSubtrees(self, root):
        d = defaultdict(int)
        res = []

        def traverse(node):
            if not node:
                return ""
            rep = "((" + traverse(node.left) + ")(" + \
                str(node.val) + ")(" + traverse(node.right) + "))"
            d[rep] += 1
            if d[rep] == 2:
                res.append(node)
            return rep

        traverse(root)
        return res
