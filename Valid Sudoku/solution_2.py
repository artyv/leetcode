class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        aux = []

        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value != '.':
                    aux += [(i, value), (value, j), (i//3, j//3, value)]
                    if len(set(aux)) != len(aux):
                        return False
        return True