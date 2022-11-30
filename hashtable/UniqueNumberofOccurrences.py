class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        cnts = set()
        for k, v in counter.items():
            if v in cnts:
                return False
            cnts.add(v)
        return True
