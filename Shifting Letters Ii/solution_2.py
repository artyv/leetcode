class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        l = len(s)
        aux = [0] * l

        for start, end, d in shifts:
            delta = 1 if d == 1 else -1
            for i in range(start, end+1):
                aux[i] += delta

        for i in range(l):
            temp = ord(s[i]) + aux[i]
            while temp > 122:
                temp -= 26
            while temp < 97:
                temp += 26
            aux[i] = chr(temp) 
        return ''.join(aux)