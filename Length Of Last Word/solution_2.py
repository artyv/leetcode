class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        s = s.strip()
        for i in range(len(s)-1, -1, -1):
            if s[i].isspace():
                return l
            l += 1
        return l