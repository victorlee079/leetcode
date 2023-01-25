class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        dist = {}

        def dfs1(node, distance):
            if node in dist or node == -1:
                return
            else:
                dist[node] = distance
                dfs1(edges[node], distance + 1)
        dfs1(node1, 0)

        ans = []

        def dfs2(node, distance):
            if node in dist:
                ans.append((max(distance, dist[node]), node))
            if edges[node] == -1:
                return

            next = edges[node]
            edges[node] = -1
            dfs2(next, distance + 1)
        dfs2(node2, 0)
        if not ans:
            return -1
        ans = sorted(ans)
        return ans[0][1]

    def closestMeetingNodeON(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        visited1 = [0] * n
        visited2 = [0] * n
        dist1 = [inf] * n
        dist2 = [inf] * n

        def dfs(node, dist, visited, distance):
            if visited[node] or node == -1:
                return
            visited[node] = 1
            dist[node] = distance
            dfs(edges[node], dist, visited, distance + 1)

        dfs(node1, dist1, visited1, 0)
        dfs(node2, dist2, visited2, 0)

        min_dist = inf
        ans = -1
        for i in range(n):
            max_dist = max(dist1[i], dist2[i])
            if max_dist < min_dist:
                ans, min_dist = i, max_dist
        return ans
