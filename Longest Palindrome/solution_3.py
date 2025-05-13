class Solution:
    def longestPalindrome(self, s: str) -> int:
        lmax = 0
        counter = set()
        for c in s:
            if c in counter:
                counter.remove(c)
                lmax += 2
            else:
                counter.add(c)
        return lmax + (len(counter) > 0)
