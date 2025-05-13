class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s

        rows = [''] * numRows
        step = -1; index = 0

        for char in s:
            if index == 0 or index == numRows - 1:
                step = -step
            rows[index] += char
            index += step
        
        return ''.join(rows)