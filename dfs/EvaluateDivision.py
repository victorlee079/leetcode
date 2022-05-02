class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            d[a][b] = v
            d[b][a] = 1 / v
        ans = []

        def dfs(ret, a, b, visited):
            if a not in d or b not in d:
                return None
            if a == b:
                return ret

            for k in d[a]:
                if (a, k) not in visited:
                    intermediate = ret * d[a][k]
                    visited.add((a, k))
                    temp = dfs(intermediate, k, b, visited)
                    if temp is not None:
                        return temp
                    visited.remove((a, k))

            return None

        for a, b in queries:
            value = dfs(1, a, b, set())
            if value is None:
                ans.append(-1.0)
            else:
                ans.append(value)
        return ans