class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        counter = Counter(tops+bottoms)
        n = len(tops)

        check = [x for x, v in counter.items() if v >= n]

        res = -1
        for c in check:
            for i in range(n):
                if tops[i] != c and bottoms[i] != c:
                    break
            else:
                res = min(tops.count(c), n-tops.count(c))
            

        return res