class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1); m = len(word2)
        d = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for column in range(1, n + 1):
            d[0][column] = column

        for row in range(1, m + 1):
            d[row][0] = row
        
        for column in range(1, n + 1):
            for row in range(1, m + 1):
                if word2[row-1] == word1[column-1]:
                    d[row][column] = d[row-1][column-1]
                else:
                    d[row][column] = 1 + min(d[row-1][column], d[row][column-1], d[row-1][column-1]) # deletion, insertion, substitution
        return d[-1][-1]