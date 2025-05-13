class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid); n = len(grid[0])
        aux = [[0 for _ in range(n)] for _ in range(m)]
        aux[0][0] = grid[0][0]
        for column in range(1, n):
            aux[0][column] = aux[0][column-1] + grid[0][column]
                
        for row in range(1, m):
            aux[row][0] = aux[row-1][0] + grid[row][0]

        for row in range(1, m):
            for column in range(1, n):
                aux[row][column] = min(aux[row][column-1], aux[row-1][column]) + grid[row][column]
        
        return aux[-1][-1]