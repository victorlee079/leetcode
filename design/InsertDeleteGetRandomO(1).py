class RandomizedSet:

    def __init__(self):
        self.map = defaultdict(int)
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.arr.append(val)
            self.map[val] = len(self.arr)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.map:
            idx = self.map[val]
            lv = self.arr[-1]
            self.map[lv] = idx
            self.arr[idx] = lv
            self.map.pop(val)
            self.arr.pop()
            return True
        return False

    def getRandom(self) -> int:
        idx = random.randint(1, len(self.arr)) - 1
        return self.arr[idx]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
