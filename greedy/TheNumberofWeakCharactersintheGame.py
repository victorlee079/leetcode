class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties = sorted(properties, key=lambda e: (-e[0], e[1]))
        ans = 0
        max_attack, max_defence = properties[0]
        for i in range(1, len(properties)):
            if properties[i][0] < max_attack and properties[i][1] < max_defence:
                ans += 1
            else:
                max_defence = properties[i][1]
        return ans