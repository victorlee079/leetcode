class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        visited = set()

        if end not in bank:
            return -1

        def canMutate(a, b):
            if len(a) != len(b):
                return False
            
            changed = False
            for c1, c2 in zip(a, b):
                if c1 != c2:
                    if changed:
                        return False
                    else:
                        changed = True
            return True

        q = deque()
        q.append(start)
        ret = 0
        while q:
            n = len(q)
            ret += 1
            for i in range(n):
                s = q.popleft()
                for b in bank:
                    if b not in visited and canMutate(s, b):
                        if b == end:
                            return ret
                        else:
                            q.append(b)
                            visited.add(b)

        return -1
