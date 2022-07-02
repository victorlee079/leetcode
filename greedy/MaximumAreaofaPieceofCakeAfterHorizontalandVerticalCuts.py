class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        ans = 0
        horizontalCuts.sort()
        verticalCuts.sort()

        maxW = horizontalCuts[0]
        for i in range(1, len(horizontalCuts)):
            maxW = max(maxW, horizontalCuts[i] - horizontalCuts[i - 1])
        maxW = max(maxW, h - horizontalCuts[-1])

        maxV = verticalCuts[0]
        for i in range(1, len(verticalCuts)):
            maxV = max(maxV, verticalCuts[i] - verticalCuts[i - 1])
        maxV = max(maxV, w - verticalCuts[-1])

        return maxW * maxV % 1000000007