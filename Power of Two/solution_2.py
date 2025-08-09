class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return format(n, '0b').count('1') == 1 if n >= 0 else False
