class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        N = 26; asc = 65
        s = ''

        while columnNumber:
            s += chr((columnNumber - 1) % N + asc)
            columnNumber = (columnNumber - 1) // N
        
        return s[::-1]