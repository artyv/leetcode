class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows, cols  = len(matrix), len(matrix[0])
        dp = [[0]*(cols + 1) for _ in range(rows + 1)]
        res = 0

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]:
                    dp[row+1][col+1] = min(dp[row][col], dp[row][col+1], dp[row+1][col]) + 1
                    res += dp[row+1][col+1]
        return res