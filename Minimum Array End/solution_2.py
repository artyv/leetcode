class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        pos = 1
        n -= 1
        while n:
            if not (x & pos):
                res |= (n & 1) * pos
                n //= 2
            pos *= 2
        return res

        