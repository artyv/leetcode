class Solution:
    def minSteps(self, n: int) -> int:
        counter = 0
        for x in range(2, int(sqrt(n)) + 1):
            while n % x == 0:
                n //= x
                counter += x
        if n > 1:
            counter += n
        return counter