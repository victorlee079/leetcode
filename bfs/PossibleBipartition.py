class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for a, b in dislikes:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)

        colors = [-1] * n
        
        # Return True if failed
        def bfs(i):
            curr = colors[i] = 0
            q = deque(graph[i])
            while q:
                # Marking the connected node as the opposite color
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

    def possibleBipartitionUnionFind(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for a, b in dislikes:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)

        parents = [i for i in range(n)]

        def find(i):
            if i != parents[i]:
                parents[i] = find(parents[i])
            return parents[i]

        def union(i, p):
            parents[find(i)] = p

        for i in range(n):
            i_parent = find(i)
            if i in graph:
                first_parent = find(graph[i][0])
                for j in graph[i][1:]:
                    union(j, first_parent)
                    if i_parent == find(j):
                        return False

        return True
