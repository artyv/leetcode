class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ''
        for i,c in enumerate(s):
            if i in spaces:
                res += ' '
            res += c
        return res