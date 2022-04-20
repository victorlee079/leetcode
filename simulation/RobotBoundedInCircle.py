class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        di = (0, 1)
        for c in instructions:
            if c == "G":
                x += di[0]
                y += di[1]
            elif c == "L":
                di = (-di[1], di[0])
            elif c == "R":
                di = (di[1], -di[0])
        return di != (0, 1) or (x == 0 and y == 0)