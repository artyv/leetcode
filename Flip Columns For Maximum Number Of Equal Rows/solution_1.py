class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        a = {}

        for row in matrix:
            pattern = ''.join('T' if x == row[0] else 'F' for x in row)
            a[pattern] = (a.get(pattern, 0)) + 1
        
        return max(a.values())