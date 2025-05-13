class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 1; counter = 0
        if flowerbed[i-1] == 0 and flowerbed[i] == 0:
            flowerbed[i-1] = 1
            counter += 1
        while i < len(flowerbed) - 1:
            if all(flowerbed[j] == 0 for j in (i-1, i, i+1)):
                flowerbed[i] = 1
                counter += 1
                i += 2
            else:
                i += 1
        if flowerbed[-2] == 0 and flowerbed[-1] == 0:
            flowerbed[-1] = 1
            counter += 1
        if counter >= n:
            return True
        return False