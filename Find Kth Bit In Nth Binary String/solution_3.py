class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            l = len(s)
            return str(format(2**l-1 - int(s, 2), '0b'))

        s = '0'
        for _ in range(n-1):
            s += '1' + invert(s)[::-1]
            if len(s) >= k:
                break
        return s[k-1]