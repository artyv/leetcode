class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s = s*2
        return goal in s