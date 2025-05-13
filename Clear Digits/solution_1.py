class Solution:
    def clearDigits(self, s: str) -> str:
        while s and not s.isalpha():
            for i in range(len(s)):
                if s[i].isdigit():
                    if i > 0:
                        s = s.replace(s[i-1]+s[i], '')
                    else:
                        s = s[1:]
                    break
        return s