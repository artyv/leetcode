class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or x == 1:
            return 1.0
        elif x == 0:
            return 0.0
        elif n == 1:
            return x
        
        if n < 0:
            x = 1/x
            n = -n
        
        res = 1
        while n:
            if n % 2 == 1:
                res *= x
            n //= 2
            x *= x
        return res