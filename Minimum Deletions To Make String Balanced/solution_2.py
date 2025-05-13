class Solution:
    def minimumDeletions(self, s: str) -> int:
        dmin = 0
        counter_b = 0
        for c in s:
            if c == 'b':
                counter_b += 1
            elif counter_b:
                dmin += 1
                counter_b -= 1

        return dmin