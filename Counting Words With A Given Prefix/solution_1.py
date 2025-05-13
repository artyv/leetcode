class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        counter = 0
        for word in words:
            counter += word.startswith(pref)
        return counter