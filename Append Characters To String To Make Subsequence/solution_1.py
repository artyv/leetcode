class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        while i < len(t) and t[:i+1] in s:
            i += 1
        if i == len(t):
            return 0
        else:
            return len(t) - i