class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        char_count = [0] * 26
        for char in tiles:
            char_count[ord(char) - ord("A")] += 1

        return self.find_sequences(char_count)

    def find_sequences(self, char_count: list) -> int:
        total = 0

        # Try using each available character
        for pos in range(26):
            if char_count[pos] == 0:
                continue

            total += 1
            char_count[pos] -= 1
            total += self.find_sequences(char_count)
            char_count[pos] += 1

        return total