class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        self.ans = 1
        g = defaultdict(list)

        for i in range(1, len(parent)):
            a, b = i, parent[i]
            g[a].append(b)
            g[b].append(a)

        def dfs(node, parent):
            # Base case
            max_len = 1

            child_lens = []
            for child in g[node]:
                if child != parent:
                    ret = dfs(child, node)
                    # Only consider two adjacent nodes with different characters
                    if s[node] != s[child]:
                        child_lens.append(ret)

            # Possible path
            if child_lens:
                # Largest go first
                child_lens = sorted(child_lens, reverse=True)
                # Longest downward path
                max_len += child_lens[0]
                self.ans = max(self.ans, max_len)
                # A path can be constructed by 2 subpaths and 1 root node
                if len(child_lens) >= 2:
                    self.ans = max(self.ans, sum(child_lens[0:2]) + 1)
            return max_len
        dfs(0, None)
        return self.ans
