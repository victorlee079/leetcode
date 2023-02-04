class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n2 < n1:
            return False
        count1 = Counter(s1)
        count2 = Counter(s2[:n1])
        for i in range(n1, len(s2)):
            if count1 == count2:
                return True
            add = s2[i]
            remove = s2[i-n1]
            count2[remove] -= 1
            if count2[remove] == 0:
                del count2[remove]
            if add not in count2:
                count2[add] = 0
            count2[add] += 1
        return count1 == count2
