class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            s_inv = ''
            for c in s:
                if c == '0':
                    s_inv += '1'
                else:
                    s_inv += '0'
            return s_inv

        s = '0'
        for _ in range(n-1):
            s += '1' + invert(s)[::-1]
        return s[k-1]