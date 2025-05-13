class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ''
        spaces = set(spaces)
        for i,c in enumerate(s):
            if i in spaces:
                res += ' '
            res += c
        return res