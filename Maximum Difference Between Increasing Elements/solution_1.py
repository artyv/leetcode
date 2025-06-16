class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        xmin = nums[0]
        dmax = -1
        for x in nums:
            if x > xmin:
                dmax = max(dmax, x - xmin)
            xmin = min(xmin, x)
        
        return dmax
