class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        ans = 0
        for k, v in counter.items():
            if v < 2:
                return -1
            ans += v // 3
            if v % 3 != 0:
                ans += 1
        return ans
