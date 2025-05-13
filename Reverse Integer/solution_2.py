class Solution:
    def reverse(self, x: int) -> int:
        x = int(str(abs(x))[::-1]) * (1 if x > 1 else -1)
        if -2**31 <= x < 2**31:
            return x
        return 0