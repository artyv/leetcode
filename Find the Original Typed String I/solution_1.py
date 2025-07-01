class Solution:
    def possibleStringCount(self, word: str) -> int:
        total = 1
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                total += 1
        return total
