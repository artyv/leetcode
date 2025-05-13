class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n > len(flowerbed):
            return False
        
        if n == 0:
            return True
        
        if len(flowerbed) == 1:
            return flowerbed[0] == 0 
        
        i = 0
 
        while i < len(flowerbed):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] == 1
                    n -= 1
            elif 0 < i < len(flowerbed) - 2:
                if flowerbed[i] == 0:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                        if n == 0:
                            return True
            else:
                if flowerbed[-2] == 0 and flowerbed[-1] == 0:
                    flowerbed[-1] = 1
                    n -= 1
            i += 2

        return n <= 0