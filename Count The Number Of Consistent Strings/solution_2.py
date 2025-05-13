class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter = 0

        for word in words:
            if all(c in allowed for c in word):
                counter += 1
        return counter