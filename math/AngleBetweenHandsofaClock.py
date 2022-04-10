class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
        hr = (hour + minutes / 60) / 12 * 360
        mi = minutes / 60 * 360
        an = abs(hr - mi)
        if 360 - an > an:
            return an
        else:
            return 360 - an