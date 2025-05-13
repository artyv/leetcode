class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or x == 1:
            return 1.0
        elif x == 0:
            return 0.0

        sign = -1 if n < 0 else 1
        res = 1
        for _ in range(abs(n)):
            res *= x
        
        if sign < 0:
            return 1/res
        return res