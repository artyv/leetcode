class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix); n = len(matrix[0])
        kmax = 0

        for row in range(m):
            for column in range(n):
                k = 0
                if matrix[row][column] == '1':
                    k = 1; i = 1
                    while row + i < m and column + i < n and matrix[row+i][column] == '1' and matrix[row][column+i] == '1':
                        k += 1; i += 1
                    kmax = max(kmax, k)

        return kmax**2  