class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        if all((s[i] + s[i+1]) in ('()', '[]', '{}') for i in range(0, len(s) - 1, 2)):
            return True
        return False