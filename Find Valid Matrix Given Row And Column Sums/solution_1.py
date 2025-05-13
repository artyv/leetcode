class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum)
        matrix = [[0] * m for _ in range(n)]
        i, j = 0, 0

        while i < n and j < m:
            matrix[i][j] = min(rowSum[i], colSum[j])
            rowSum[i] -= matrix[i][j]
            colSum[j] -= matrix[i][j]

            if rowSum[i] == 0: 
                i += 1
            if colSum[j] == 0: 
                j += 1
        
        return matrix

