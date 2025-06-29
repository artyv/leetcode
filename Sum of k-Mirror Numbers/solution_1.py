class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def gen_palindromes():
            for i in range(1, 10):
                yield i
            length = 2
            while True:
                half_len = (length + 1) // 2
                for half in range(10**(half_len - 1), 10**half_len):
                    s = str(half)
                    if length % 2 == 0:
                        pal = s + s[::-1]
                    else:
                        pal = s + s[-2::-1]
                    yield int(pal)
                length += 1
        
        xsum = 0
        counter = 0
        for x in gen_palindromes():
            s = self.convert_reverse(x, k)
            if s == s[::-1]:
                xsum += x
                counter += 1
                if counter == n:
                    break
        return xsum

    def convert_reverse(self, x, base):
        s = ''
        while x:
            s += str(x % base)
            x //= base
        return s
