class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        if l == 1:
            return False
        
        for n in range(1, l//2 + 1):
            if l % n == 0:
                if s[:n] * (l // n) == s:
                    return True
        
        return False