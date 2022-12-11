class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        dirs = [0, 1, 0, -1, 0]
        m, n = len(maze), len(maze[0])
        maze[entrance[0]][entrance[1]] = '+'
        q = deque([entrance])
        steps = 0
        while q:
            l = len(q)
            for i in range(l):
                r, c = q.popleft()
                for j in range(4):
                    next_r, next_c = r + dirs[j], c + dirs[j+1]
                    if -1 < next_r < m and -1 < next_c < n and maze[next_r][next_c] != '+':
                        # Earlier Termination
                        if next_r == m-1 or next_r == 0 or next_c == n-1 or next_c == 0:
                            return steps + 1
                        maze[next_r][next_c] = '+'
                        q.append([next_r, next_c])
            steps += 1

        return -1
        
    def nearestExitSlower(self, maze: List[List[str]], entrance: List[int]) -> int:
        dirs = [0, 1, 0, -1, 0]
        m, n = len(maze), len(maze[0])
        q = deque([entrance])
        steps = 0
        while q:
            l = len(q)
            for i in range(l):
                r, c = q.popleft()
                if steps > 0 and (r == m-1 or r == 0 or c == n-1 or c == 0):
                    return steps
                maze[r][c] = '+'
                for j in range(4):
                    next_r, next_c = r + dirs[j], c + dirs[j+1]
                    if -1 < next_r < m and -1 < next_c < n and maze[next_r][next_c] != '+':
                        q.append([next_r, next_c])
            steps += 1

        return -1
