class Solution:
    def minChanges(self, s: str) -> int:
        counter = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i+1]:
                counter += 1
        
        return counter