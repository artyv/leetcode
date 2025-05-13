class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        sign = 1

        if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
            sign = -1
        
        dividend, divisor = abs(dividend), abs(divisor)

        result = 0
        if divisor == 1: 
            if sign == -1 and sign * dividend < -2**31:
                return -2**31
            elif sign == 1 and sign * dividend > 2**31 - 1:
                return 2**31 - 1
            else:
                return sign * dividend

        for _ in range(dividend, divisor-1, -divisor):
            result += 1
        
        if sign * result < -2**31:
            return -2**31
        elif sign * result > 2**31 - 1:
            return 2**31 - 1
        return sign * result
