class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        counter = Counter(s1)
        my_set = set(s1)
        for i in range(len(s2)-l+1):
            if set(s2[i:i+1]).issubset(my_set) and Counter(s2[i:i+l]) == counter:
                return True
        
        return False