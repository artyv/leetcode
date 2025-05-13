class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        def check(a, n):
            for i in range(n):
                if any(a[i].count(x) > 1 for x in a[i] if x.isdigit()):
                    return False
            return True

        if check(board, n) and check(list(zip(*board)), n) and check([board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3] for j in range(0, n, 3) for i in range(0, n, 3)], n):
            return True
        return False