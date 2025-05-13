class Solution:
    def longestPalindrome(self, s: str) -> int:
        lmax = 0
        counter = [x for x in Counter(s).values()]
        for x in counter:
            lmax += (x // 2) * 2

        return lmax + any(x % 2 == 1 for x in counter)
