class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        # Tricky solution using Legendre's formula
        trailing_zeros = sum(n//5**i for i in range (1, int(math.log(n, 5))+1))
        
        return trailing_zeros