class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        d = {
            '0': 0,
            '110': 1,
            '1110': 2,
            '11110': 3
        }
        
        idx = 0
        while idx < len(data):
            c = '{0:08b}'.format(data[idx])[-9:]
            rem = -1
            for key, value in d.items():
                if c.startswith(key):
                    rem = value
                    break
            if rem < 0:
                return False
            for i in range(rem):
                idx += 1
                if idx >= len(data):
                    return False
                c = '{0:08b}'.format(data[idx])[-9:]
                if not c.startswith("10"):
                    return False
            idx += 1
        return True
