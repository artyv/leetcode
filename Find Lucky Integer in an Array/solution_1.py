class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        freq = Counter(arr)
        for k,v in freq.items():
            if k == v and k > res:
                res = k
        return res
