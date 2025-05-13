class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        #N = 26; asc = 65
        s = ''

        while columnNumber:
            columnNumber -= 1
            s += chr(columnNumber % 26 + 65)
            columnNumber //= 26
        
        return s[::-1]