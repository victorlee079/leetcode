class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        d = {}
        d[(p, 0)] = 0
        d[(p, p)] = 1
        d[(0, p)] = 2

        curr = (p, q)
        up = True

        while curr not in d:
            (a, b) = curr
            a = 0 if a == p else p
            if up:
                if b + q > p:
                    b = p - (b + q - p)
                    up = False
                else:
                    b += q
            else:
                if b - q < 0:
                    b = q - b
                    up = True
                else:
                    b -= q

            curr = (a, b)

        return d[curr]