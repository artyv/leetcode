class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[-1]*m for _ in range(n)]

        def traverse(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            
            max_steps = 0

            # right up
            if i >= 1 and j < m-1 and grid[i][j] < grid[i-1][j+1]:
                max_steps = max(max_steps, 1 + traverse(i-1, j+1))
            # right
            if j < m-1 and grid[i][j] < grid[i][j+1]:
                max_steps = max(max_steps, 1 + traverse(i, j+1))
            # right down
            if i < n-1 and j < m-1 and grid[i][j] < grid[i+1][j+1]:
                max_steps = max(max_steps, 1 + traverse(i+1, j+1))
            
            dp[i][j] = max_steps
            return max_steps
        
        max_res = 0
        for i in range(n):
            max_res = max(max_res, traverse(i, 0))
        
        return max_res
        
        max_steps = 0
        for i in range(n):
            max_steps = max(max_steps, traverse[i, 0, 0, 0])
        
        return max_steps