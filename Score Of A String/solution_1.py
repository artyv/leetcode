class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_sum = 0
        for i in range(len(s)-1):
            ascii_sum += abs(ord(s[i])-ord(s[i+1]))
        return ascii_sum