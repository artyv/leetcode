class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counter = 0
        for row in matrix:
            if row.count(0) > 0 and row.count(1) > 0:
                counter += 1
        return counter