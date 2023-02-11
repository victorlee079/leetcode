class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in redEdges:
            graph[a].append((b, 1))
        for u, v in blueEdges:
            graph[u].append((v, 2))

        ans = [-1] * n
        ans[0] = 0
        q = deque([(0, 1), (0, 2)])
        visited = set()
        visited.add((0, 1))
        visited.add((0, 2))
        step = 0
        while q:
            step += 1
            size = len(q)
            for _ in range(size):
                curr_node, prev_color = q.popleft()
                for node, color in graph[curr_node]:
                    if color != prev_color and (node, color) not in visited:
                        ans[node] = min(
                            step, ans[node]) if ans[node] != -1 else step
                        q.append((node, color))
                        visited.add((node, color))
        return ans
