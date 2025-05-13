class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        dp = [[0] * m for _ in range(n)]
        
        # 1 row
        for col in range(1, m):
            dp[0][col] = max(dp[0][col-1], moveTime[0][col]) + 1
        
        # 1 column
        for row in range(1, n):
            dp[row][0] = max(dp[row-1][0], moveTime[row][0]) + 1
        
        for row in range(1, n):
            for col in range(1, m):
                dp[row][col] = max(min(dp[row-1][col], dp[row][col-1]), moveTime[row][col]) + 1
    
        return dp[n-1][m-1]