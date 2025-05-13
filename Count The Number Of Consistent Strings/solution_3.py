class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter = 0
        words = list(map(set, words))

        for word in words:
            for letter in word:
                if letter not in allowed:
                    break
            else:
                counter += 1
        return counter