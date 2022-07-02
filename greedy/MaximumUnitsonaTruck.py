class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda boxType: boxType[1], reverse=True)

        ans = 0
        for b in boxTypes:
            if truckSize < 1:
                break

            if truckSize >= b[0]:
                ans += b[0] * b[1]
                truckSize -= b[0]
            else:
                ans += truckSize * b[1]
                truckSize = 0

        return ans