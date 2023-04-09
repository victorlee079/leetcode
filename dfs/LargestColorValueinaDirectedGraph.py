class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        for a, b in edges:
            d[a].append(b)

        mem = {}
        self.ans = -1

        def dfs(node, path):
            if node in path:
                return None
            if node in mem:
                return mem[node]
            path.add(node)

            res = defaultdict(int)
            for b in d[node]:
                child_res = dfs(b, path)
                if child_res is None:
                    return None
                for c, v in child_res.items():
                    res[c] = max(res[c], v)

            path.remove(node)
            res[colors[node]] += 1
            mem[node] = res
            return res

        ans = 0
        for i in range(len(colors)):
            temp = dfs(i, set())
            if temp == None:
                return -1
            ans = max(ans, max(temp.values()))
        return ans
