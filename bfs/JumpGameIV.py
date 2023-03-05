class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        d = defaultdict(list)
        for j in range(n):
            d[arr[j]].append(j)

        visited = [0] * n
        q = deque([0])
        steps = -1
        while q:
            steps += 1
            size = len(q)
            for _ in range(size):
                i = q.popleft()
                visited[i] = 1
                if i == n-1:
                    return steps
                if i-1 > -1 and not visited[i-1]:
                    q.append(i-1)
                if i+1 < n and not visited[i+1]:
                    q.append(i+1)
                for j in d[arr[i]]:
                    if j != i and not visited[j]:
                        q.append(j)
                d[arr[i]].clear()

        return -1
