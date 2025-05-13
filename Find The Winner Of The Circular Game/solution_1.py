class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(1, n+1))
        index = 0
        while len(players) > 1:
            steps = k % (len(players) + 1)
            if steps == 0:
                index -= 1
            else:
                index = (index + steps - 1) % len(players)
            players.pop(index)
        return players[0]