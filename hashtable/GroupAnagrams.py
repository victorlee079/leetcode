class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            t = "".join(sorted(s))
            d[t].append(s)
        return d.values()
