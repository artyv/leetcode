class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_end = min_end = smax = smin = nums[0]
        l = len(nums)

        for i in range(1, l):
            max_end = max(max_end + nums[i], nums[i])
            smax = max(smax, max_end)
        
        for i in range(1, l):
            min_end = min(min_end + nums[i], nums[i])
            smin = min(smin, min_end)
        
        return max(abs(smin), abs(smax))


