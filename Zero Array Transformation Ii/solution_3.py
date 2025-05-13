class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        d = {}

        for i,x in enumerate(nums):
            if x != 0:
                d[i] = x
        
        for i, (l, r, val) in enumerate(queries):
            for key in d.keys():
                if key in range(l, r+1):
                    d[key] -= val
            
            d = {k:v for k,v in d.items() if v > 0}
            if not d:
                return i+1
        
        return -1
        