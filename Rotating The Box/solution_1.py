class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n = len(box[0])
        m = len(box)

        grid = [['.'] * m for _ in range(n)]

        for r in range(m):
            i = n - 1
            for c in reversed(range(n)):
                if box[r][c] == '#':
                    grid[i][m-r-1] = '#'
                    i -= 1
                elif box[r][c] == '*':
                    grid[c][m-r-1] = '*'
                    i = c - 1
        return grid