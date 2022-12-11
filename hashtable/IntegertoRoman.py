d = {}
d[1000] = "M"
d[900] = "CM"
d[500] = "D"
d[400] = "CD"
d[100] = "C"
d[90] = "XC"
d[50] = "L"
d[40] = "XL"
d[10] = "X"
d[9] = "IX"
d[5] = "V"
d[4] = "IV"
d[1] = "I"

class Solution:
    def intToRoman(self, num: int) -> str:
        s = []
        for k in d.keys():
            cnt = num // k
            num = num % k
            for i in range(cnt):
                s.append(d[k])
            if num == 0:
                break
        return ''.join(s)

