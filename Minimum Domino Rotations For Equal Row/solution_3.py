class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        for x in range(1, 6+1):
            if all(x == tops[i] or x == bottoms[i] for i in range(n)):
                return min(n - tops.count(x), n - bottoms.count(x))
        
        return -1