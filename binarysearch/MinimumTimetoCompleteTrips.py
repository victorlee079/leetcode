class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 1, max(time) * totalTrips

        def isValid(t):
            cnt = 0
            for i in range(len(time)):
                cnt += t // time[i]
            return cnt >= totalTrips

        while l < r:
            m = l + (r - l) // 2
            if isValid(m):
                r = m
            else:
                l = m + 1
        return l
