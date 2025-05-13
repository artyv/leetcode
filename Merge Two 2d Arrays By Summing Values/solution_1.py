class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = {}
        for i, x in nums1:
            if i in res:
                res[i] += x
            else:
                res[i] = x
        
        for i, x in nums2:
            if i in res:
                res[i] += x
            else:
                res[i] = x
        
        return sorted([[i, x] for (i, x) in res.items()], key=lambda x: x[0])