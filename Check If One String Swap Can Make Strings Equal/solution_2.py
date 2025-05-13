class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if sorted(s1) != sorted(s2):
            return False
        counter = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                counter += 1
        
        return False if counter % 2 != 0 else True