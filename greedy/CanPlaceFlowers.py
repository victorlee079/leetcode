class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left, right = False, False
                if -1 < i - 1:
                    left = flowerbed[i-1] == 1
                if i + 1 < len(flowerbed):
                    right = flowerbed[i+1] == 1
                if not left and not right:
                    cnt += 1
                    flowerbed[i] = 1
        return n <= cnt
