class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        res = []
        high = n-1
        r = 0
        
        for i, val in enumerate(nums):
            if val == key:
                l = max(r, i-k)
                r = min(high, i+k) + 1
                for j in range(l, r):
                    res.append(j)

        return res
