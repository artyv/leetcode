class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]; b = b[::-1]
        accum = 0
        reversed_output = ''
        len_a = len(a); len_b = len(b)
        min_len = min(len_a, len_b)
        for i in range(min_len):
            reversed_output += str((int(a[i]) + int(b[i]) + accum) % 2)
            accum = (int(a[i]) + int(b[i]) + accum) // 2
        if len_a < len_b:
            for j in range(min_len, len_b):
                reversed_output += str((int(b[j]) + accum) % 2)
                accum = (int(b[j]) + accum) // 2
        elif len_a > len_b:
            for j in range(min_len, len_a):
                reversed_output += str((int(a[j]) + accum) % 2)
                accum = (int(a[j]) + accum) // 2

        if accum != 0:
            reversed_output += str(accum)
        return reversed_output[::-1]