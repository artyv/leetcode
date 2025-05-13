class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return sorted(Counter(s).values()) == sorted(Counter(t).values())