class Solution:
    def minimumDeletions(self, s: str) -> int:
        dmin = 10**10
        # while s[counter] == 'b':
        #     counter += 1
        for i in range(len(s)):
            counter = s[:i].count('b') + s[i+1:].count('a')
            dmin = min(dmin, counter)
        return dmin