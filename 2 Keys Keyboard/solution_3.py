class Solution:
    def minSteps(self, n: int) -> int:
        def is_prime(n):
            for x in range(2, int(sqrt(n))+1):
                if n % x == 0:
                    return False
            else:
                return True
        
        if n == 1:
            return 0
        if n % 2 == 1:
            if is_prime(n):
                return n
        else:
            if math.log2(n).is_integer():
                return 2 * math.log2(n)
        counter = 0
        while n > 1:
            for x in range(2, int(sqrt(n))+1):
                while n % x == 0:
                    n //= x
                    counter += x
        return counter