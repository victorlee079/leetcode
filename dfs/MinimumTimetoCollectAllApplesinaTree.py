class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        if not any(hasApple):
            return 0

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        marks = set()
        visited = set()
        visited.add(0)

        def dfs(path, node):
            if hasApple[node]:
                marks.update(path)

            for b in g[node]:
                if b not in visited:
                    path.append(b)
                    visited.add(b)
                    dfs(path, b)
                    path.pop()

        dfs([0], 0)

        return (len(marks)-1) * 2
