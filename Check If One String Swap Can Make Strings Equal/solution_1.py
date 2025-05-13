class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        counter = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                counter += 1
                if counter > 2:
                    return False
        return True