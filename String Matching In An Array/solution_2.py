class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        s = ''.join(words)
        res = [word for word in words if s.count(word) > 1]
        return res