class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #return chr(sum(list(map(ord, t))) - sum(list(map(ord, s))))
        for c in t:
            if s.count(c) < t.count(c):
                return c 