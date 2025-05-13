class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0; start = 0
        while i < len(t) and start <= len(s)-1 and s.find(t[i], start) != -1:
            start = s.find(t[i], start) + 1
            i += 1

        if i == len(t):
            return 0
        else:
            return len(t) - i