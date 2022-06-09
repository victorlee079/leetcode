class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)
        for cpdomain in cpdomains:
            num, domain = cpdomain.split(" ")
            num = int(num)
            names = domain.split(".")
            key = ""
            for i in range(len(names)-1, -1, -1):
                if key:
                    key = "." + key
                key = names[i] + key
                d[key] += num
        ret = []
        for key, value in d.items():
            ret.append(str(value) + " " + key)
        return ret
