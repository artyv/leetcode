class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        null_rows = set(); null_columns = set();
        m = len(matrix); n = len(matrix[0])

        for row in range(m):
            for column in range(n):
                if matrix[row][column] == 0:
                    null_rows.add(row)
                    null_columns.add(column)

        for row in null_rows:
            matrix[row] = [0]*n
        
        for row in range(m):
            if row not in null_rows:
                for column in null_columns:
                    matrix[row][column] = 0


        

