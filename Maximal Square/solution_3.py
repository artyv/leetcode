class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix); n = len(matrix[0])
        aux = [[0 for _ in range(n)] for _ in range(m)]
        kmax = 0

        for row in range(m):
            for column in range(n):
                k = 0
                if matrix[row][column] == '1':
                    if row == 0 or column == 0:
                        aux[row][column] = 1
                    else:
                        aux[row][column] = min(aux[row-1][column], aux[row][column-1], aux[row-1][column-1]) + 1
  
                    kmax = max(kmax, aux[row][column])

        return kmax**2  