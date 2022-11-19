class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = defaultdict(list)
        columns = defaultdict(list)
        for x, y in stones:
            rows[x].append((x, y))
            columns[y].append((x, y))
        
        visited = set()
        def dfs(stone):
            x, y = stone
            if (x, y) in visited:
                return 0
            
            visited.add((x, y))
            cnt = 1
            for s in rows[x]:
                if s not in visited:
                    cnt += dfs(s)
            for s in columns[y]:
                if s not in visited:
                    cnt += dfs(s)
            return cnt
        
        ret = 0
        for x, y in stones:
            if (x, y) not in visited:
                cnt = dfs((x, y))
                if cnt > 1:
                    ret += cnt - 1 

        return ret
