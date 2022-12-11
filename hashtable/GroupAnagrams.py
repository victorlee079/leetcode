class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            t = "".join(sorted(s))
            d[t].append(s)
        return d.values()

    def count(self, str):
        arr = [0] * 26
        for c in str:
            arr[ord(c) - ord('a')] += 1
        return ''.join([chr(s) for s in arr])


    def groupAnagramsCount(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            k = self.count(s)
            d[k].append(s)
        return d.values()
