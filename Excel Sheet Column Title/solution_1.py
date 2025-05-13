class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        N = 26; asc = 65
        s = ''

        while columnNumber:
            columnNumber -= 1
            s += chr(columnNumber % N + asc)
            columnNumber //= N
        
        return s[::-1]