class Solution:
    def mySqrt(self, x: int) -> int:
        prev = 0
        for s in range(1, x//2 + 1):
            if s * s == x:
                return s
            elif s * s > x:
                break
            else:
                prev = s
        return prev