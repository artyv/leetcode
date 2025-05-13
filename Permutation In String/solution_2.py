class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        sorted_s = sorted(s1)
        for i in range(len(s2)-l+1):
            if sorted(s2[i:i+l]) == sorted_s:
                return True
        
        return False