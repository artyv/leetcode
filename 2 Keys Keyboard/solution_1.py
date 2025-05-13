class Solution:
    def minSteps(self, n: int) -> int:
        counter = 0
        x = 2
        while n > 1:
            while n % x == 0:
                n //= x
                counter += x
            x += 1
        return counter