class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        arr = []
        n = len(plantTime)
        for i in range(n):
            arr.append((growTime[i], i))
        arr = sorted(arr, key=lambda e: -e[0])
        plant = grow = 0
        for i in range(n):
            j = arr[i][1]
            plant += plantTime[j]
            grow = max(grow, plant + growTime[j])
        return grow
