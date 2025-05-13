class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        counter = Counter(s1)
        for i in range(len(s2)-l+1):
            if Counter(s2[i:i+l]) == counter:
                return True
        
        return False