class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(1, n+1))
        index = 0
        while len(players) > 1:
            steps = k % len(players)
            index = (index + len(players) + steps - 1) % len(players)
            players.pop(index)
            index %= len(players)
            print(f"{index=}  {players=}")
        return players[0]