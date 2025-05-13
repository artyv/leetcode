class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        obstacles = []
        n = len(obstacleGrid[0]); m = len(obstacleGrid)
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacles.append(i*n + j + 1)
        
        if (n == 1 or m == 1) and len(obstacles) == 0:
            return 1
        elif (n == 1 or m == 1):
            return 0
        
        a = [0] * ((m+1)*(n+1))
        a[1] = 1

        for i in range(1, m*n+1):
            if i in obstacles:
                a[i] = 0
            else:
                if i % n != 0:
                    a[i+1] += a[i]
                a[i+n] += a[i]
        return a[m*n]