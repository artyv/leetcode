class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(n):
            if n == 1:
                return False
            for x in range(2, int(sqrt(n))+1):
                if n % x == 0:
                    return False
            return True
        
        ans = []
        diff = 10**10
        num1 = num2 = 0

        for x in range(left, right+1):
            if is_prime(x):
                if num1 == 0:
                    num1 = x
                elif num2 == 0:
                    num2 = x
                else:
                    num1 = num2
                    num2 = x
                if abs(num2 - num1) < diff:
                    diff = abs(num2 - num1)
                    ans = [num1, num2]
        return ans if num1 != 0 and num2 != 0 else [-1, -1]