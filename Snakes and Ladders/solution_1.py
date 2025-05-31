class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        # convert num to (row, col)
        def get_pos(num):
            quot, rem = divmod(num - 1, n)
            row = n - 1 - quot
            col = rem if (quot % 2 == 0) else n - 1 - rem
            return row, col

        visited = set()
        queue = deque([(1, 0)]) # (cell_num, num_of_moves)
        while queue:
            cur, moves = queue.popleft()
            for next_num in range(cur+1, min(cur+6, n**2)+1):
                r,c = get_pos(next_num)
                if board[r][c] != -1:
                    next_num = board[r][c]
                if next_num == n**2:
                    return moves + 1
                if next_num not in visited:
                    visited.add(next_num)
                    queue.append((next_num, moves+1))
        return -1
