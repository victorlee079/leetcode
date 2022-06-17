class Solution(object):
    # 3 possible outcomes for a node
    def minCameraCoverDp(self, root):
        def solve(node):
            # 0: Strict ST; All nodes below this are covered, but not this one
            # 1: Normal ST; All nodes below and incl this are covered - no camera
            # 2: Placed camera; All nodes below this are covered, plus camera here

            if not node: return 0, 0, float('inf')
            L = solve(node.left)
            R = solve(node.right)

            dp0 = L[1] + R[1] # Immediate child nodes have no camera
            dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:])) # Either one of the immediate child nodes has a camera
            dp2 = 1 + min(L) + min(R) # This node has a camera

            return dp0, dp1, dp2

        return min(solve(root)[1:])
      
    def minCameraCover(self, root):
        self.ans = 0
        covered = {None}

        def dfs(node, parent):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
                
                # Parent is None and node is not covered
                # Either child node is not covered
                # Add a camera
                if (parent is None and node not in covered or
                        node.left not in covered or node.right not in covered):
                    self.ans += 1
                    covered.update({node, par, node.left, node.right})

        dfs(root, None)
        return self.ans
