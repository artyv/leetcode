class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(1, n+1))
        index = 0
        while n > 1:
            index = (index + k - 1) % n
            players.pop(index)
            n -= 1
            index %= n

        return players[0]