class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter = 0
        allowed = set(allowed)

        for word in words:
            if set(word).issubset(allowed):
                counter += 1
        return counter