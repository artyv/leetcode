class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        smin = smax = nums[0]
        l = len(nums)

        for i in range(l):
            cum_sum = 0
            for j in range(i, l):
                cum_sum += nums[j]

                smin = min(smin, cum_sum)
                smax = max(smax, cum_sum)
        
        return max(abs(smin), abs(smax))


