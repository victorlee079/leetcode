class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for a, b in dislikes:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)

        colors = [-1] * n

        def bfs(i):
            curr = colors[i] = 0
            q = deque(graph[i])
            while q:
                curr = 1 - curr
                l = len(q)
                for _ in range(l):
                    j = q.popleft()
                    # Not visited
                    if colors[j] == -1:
                        colors[j] = curr
                        for k in graph[j]:
                            q.append(k)
                    else:
                        if colors[j] != curr:
                            return True

            return False

        for i in range(n):
            if colors[i] == -1 and bfs(i):
                return False

        return True
