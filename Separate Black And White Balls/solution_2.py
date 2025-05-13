class Solution:
    def minimumSteps(self, s: str) -> int:
        counter = 0; count_0 = 0
        l = len(s)
        i = 1
        while i < l:
            if s[i-1]+s[i] == '10':
                j = 1
                while i+j < l and s[i+j] == '0':
                    j += 1
                counter += j
                i += j
                continue
            i += 1
        return counter