class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ss = s + s
        #just check it mathematically s = sub^n; ss = sub + sub^(2n-2) + sub; ss[1:-1] = xr + sub^(2n-2) + lx; 
        #for all n >= 2 it works; s = s^2 => ss[1:-1] = xr + s^2 + lx; indeed, s exists in ss[1:-1]

        if s in ss[1:-1]:
            return True
        return False