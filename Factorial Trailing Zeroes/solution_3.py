class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        
        i, product = 1, 1

        while i < n:
            i += 1
            product *= i
        
        trailing_zeros = 0
        while (product % 10) == 0:
            trailing_zeros += 1
            product /= 10
        
        return trailing_zeros