class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1], [1,1]]
        row = 2
        while row < numRows:
            row_a = [1] * (row+1)
            for i in range(1, row):
                row_a[i] = res[row-1][i-1] + res[row-1][i]
            res.append(row_a)
            row += 1
        return res
