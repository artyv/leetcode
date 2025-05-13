class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        output = ''
        for i in range(len(s)-2):
            if not(s[i] == s[i+1] and s[i+1] == s[i+2]):
                output += s[i]
        output += s[-2] + s[-1]
        return output