class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        
        # Put guards and walls on grid, using 7
        for x, y in guards:
            grid[x][y] = 7    
        for x, y in walls:
            grid[x][y] = 7
            
        # Directions: up, right, down, left
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # Process each guard's line of sight
        for gx, gy in guards:
            for dx, dy in dirs: # dx, dy - movement direction offsets
                x, y = gx, gy
                while True:
                    x += dx
                    y += dy
                    # Check cells in current direction until hitting boundary or obstacle
                    if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 7:
                        break
                    grid[x][y] = 1
        
        # Count unguarded cells (cells with value 0)
        return sum(row.count(0) for row in grid)
        