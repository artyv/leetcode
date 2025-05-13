class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        l = len(s)
        aux = [0] * (l+1)

        for start, end, d in shifts:
            delta = 1 if d == 1 else -1
            aux[start] += delta
            if end + 1 < l:
                aux[end + 1] -= delta

        for i in range(1, l):
            aux[i] += aux[i - 1]

        res = [0] * l
        for i in range(l):
            temp = ord(s[i]) + aux[i]
            while temp > 122:
                temp -= 26
            while temp < 97:
                temp += 26
            res[i] = chr(temp) 
        return ''.join(res)