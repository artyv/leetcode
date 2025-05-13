class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        for x in range(1, 6+1):
            if all(x == tops[i] or x == bottoms[i] for i in range(n)):
                rotations_top = sum(1 for i in range(n) if tops[i] != x)
                rotations_bottom = sum(1 for i in range(n) if bottoms[i] != x)
                return min(rotations_top, rotations_bottom)
        
        return -1