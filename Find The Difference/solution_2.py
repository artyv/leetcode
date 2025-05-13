class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(list(map(ord, t))) - sum(list(map(ord, s))))