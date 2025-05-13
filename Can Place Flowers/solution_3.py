class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n > len(flowerbed):
            return False
        
        if n == 0:
            return True
        
        if len(flowerbed) == 1:
            return flowerbed[0] == 0 
        
        i = 1;
        if flowerbed[i-1] == 0 and flowerbed[i] == 0:
            flowerbed[i-1] = 1
            n -= 1
        while i < len(flowerbed) - 1:
            if all(flowerbed[j] == 0 for j in (i-1, i, i+1)):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
                i += 2
            else:
                i += 1
        if flowerbed[-2] == 0 and flowerbed[-1] == 0:
            flowerbed[-1] = 1
            n -= 1

        return n <= 0