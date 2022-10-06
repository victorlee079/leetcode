class TimeMap:

    def __init__(self):
        self.timeMap = [(0, {})]

    # O(log n + n)
    def set(self, key: str, value: str, timestamp: int) -> None:
        i = bisect_left(self.timeMap, timestamp, key=lambda item: item[0])
        if i < len(self.timeMap):
            # Add / Update for an existing timestamp
            if self.timeMap[i][0] == timestamp:
                self.timeMap[i][1][key] = value
            else:
                self.timeMap.insert(i, (timestamp, {key: value}))
        else:
           self.timeMap.append((timestamp, {key: value}))
        

    # O(log n + n)
    def get(self, key: str, timestamp: int) -> str:
        i = bisect_left(self.timeMap, timestamp, key=lambda item: item[0])

        # Adjust 
        i = min(i, len(self.timeMap)-1)
        if self.timeMap[i][0] > timestamp:
            i -= 1
            
        for j in range(i, -1, -1):
            if key in self.timeMap[j][1]:
                return self.timeMap[j][1][key]
        return ""

class TimeMapSortedDict:

    def __init__(self):
        self.d = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        s = self.d[key]
        
        # Assignment of variables within expression
        if (i := s.bisect_right(timestamp)) > 0:
            _, v = s.peekitem(i - 1)  # "_" is the largest key in "s" which is less than or equal to "timestamp" 

            return v

        return ''

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
