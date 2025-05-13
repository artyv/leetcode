from itertools import product

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        p = product('()', repeat=2*n-2)
        output = []
        for x in p:
            s = '(' + ''.join(x) + ')'
            if s.count('(') == n and s.count(')') == n and self.validComb(s):
                output += [s]
        return output
    
    def validComb(self, t) -> bool:
        balance = 0
        for c in t:
            balance = balance + 1 if c == '(' else balance - 1
            if balance < 0:
                return False
        return True