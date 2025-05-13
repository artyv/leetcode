class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        sign = 1
        if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
            sign = -1
        
        dividend, divisor = abs(dividend), abs(divisor)

        xmin = -2**31; xmax = 2**31 - 1
        if divisor == 1: 
            return min(max(sign * dividend, xmin), xmax)

        result = len(range(dividend, divisor-1, -divisor))        
        
        return min(max(sign * result, xmin), xmax)
