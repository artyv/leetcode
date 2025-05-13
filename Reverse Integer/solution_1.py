class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        s = s[::-1] if x >= 0 else s[0]+s[:0:-1]
        x = int(s) if -2**31 <= int(s) < 2**31 else 0
        return x