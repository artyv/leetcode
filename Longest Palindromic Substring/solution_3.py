class Solution:
    def longestPalindrome(self, s: str) -> str:
        smax = s[0]
        for i in range(len(s)):
            s1 = self.findPalindrome(s, i-1, i+1)
            s2 = self.findPalindrome(s, i, i+1)
            if len(s1) > len(smax):
                smax = s1
            elif len(s2) > len(smax):
                smax = s2

        return smax

    def findPalindrome(self, s: str, j: int, k: int) -> str:
        smax = s[0]
        while j >= 0 and k < len(s):
            if s[j] != s[k]:
                return smax
            smax = s[j:k+1]
            j -= 1; k += 1
        return smax
