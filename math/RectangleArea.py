class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        rec1 = (ax2 - ax1) * (ay2 - ay1)
        rec2 = (bx2 - bx1) * (by2 - by1)

        # A contains B
        if ax1 <= bx1 <= ax2 and ax1 <= bx2 <= ax2 and ay1 <= by1 <= ay2 and ay1 <= by2 <= ay2:
            return rec1

        # B contains A
        if bx1 <= ax1 <= bx2 and bx1 <= ax2 <= bx2 and by1 <= ay1 <= by2 and by1 <= ay2 <= by2:
            return rec2
        
        # Not overlapped
        if ax1 > bx2 or bx1 > ax2 or ay1 > by2 or by1 > ay2:
            return rec1 + rec2
        # Overlapped
        else:
            cx1, cy1 = max(ax1, bx1), max(ay1, by1)
            cx2, cy2 = min(ax2, bx2), min(ay2, by2)
            rec3 = (cx2 - cx1) * (cy2 - cy1)
            return rec1 + rec2 - rec3
