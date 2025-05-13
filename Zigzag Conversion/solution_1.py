class Solution:
    def convert(self, s: str, numRows: int) -> str:
        len_s = len(s)
        if len_s <= numRows or numRows == 1:
            return s

        s_output = ''

        # add first row
        s_output += ''.join([s[j] for j in range(0, len_s, 2 * (numRows-1))])
        
        for row in range(2, numRows):
            step = 2 * (row-1)
            j = row - 1
            while j < len_s:
                s_output += s[j]
                step = 2 * (numRows-1) - step
                j += step
        
        # add last row
        s_output += ''.join([s[j] for j in range(numRows-1, len_s, 2 * (numRows-1))])
        
        return s_output