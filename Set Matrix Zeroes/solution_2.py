class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        aux = []
        m = len(matrix); n = len(matrix[0])

        for row in range(m):
            for column in range(n):
                if matrix[row][column] == 0:
                    aux.append((row, column))

        for r,c in aux:
            for x in range(n):
                matrix[r][x] = 0
            for y in range(m):
                matrix[y][c] = 0


        

