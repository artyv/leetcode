class Solution:
    def shortestPalindrome(self, s: str) -> str:
        l = len(s)
        reversed_s = s[::-1]

        for i in range(l):
            if s[:l-i] == reversed_s[i:]:
                return reversed_s[:i] + s
        return ''