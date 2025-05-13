class Solution:
    def minimumLength(self, s: str) -> int:
        d = Counter(s)
        l = 0
        for v in d.values():
            if v % 2 == 1:
                l += 1
            else:
                l += 2
        return l