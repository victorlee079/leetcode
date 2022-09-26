class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equals = defaultdict(list)
        not_equals = defaultdict(list)
        
        for equ in equations:
            equal = equ[1:3] == "=="
            v1, v2 = equ[0], equ[3]
            if equal:
                equals[v1].append(v2)
                equals[v2].append(v1)
            else:
                if v1 == v2:
                    return False
                not_equals[v1].append(v2)
        
        def dfs(visited, v1, v2):
            if v2 in equals[v1]:
                return True
            
            visited.add(v1)
            for v in equals[v1]:
                if v not in visited:
                    if dfs(visited, v, v2):
                        return True
            return False
        
        for key, vertices in not_equals.items():
            for v in vertices:
                if dfs(set(), key, v):
                    return False
                
        return True
        
    def equationsPossibleUnionFind(self, equations: List[str]) -> bool:
        not_equals = defaultdict(list)
        
        parent = {a: a for a in "abcdefghijklmnopqrstuvwxyz"}
        
        def find(v):
            if v == parent[v]:
                return v
            else:
                parent[v] = find(parent[v])
            return parent[v]
        
        for equ in equations:
            equal = equ[1:3] == "=="
            v1, v2 = equ[0], equ[3]
            if equal:
                parent[find(v1)] = find(v2)
            else:
                if v1 == v2:
                    return False
                not_equals[v1].append(v2)

        for key, vertices in not_equals.items():
            for v in vertices:
                if find(key) == find(v):
                    return False
                
        return True
        
            
            
