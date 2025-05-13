class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        # even better if we fix k only, then max when nums[i] - nums[j] is max
        x_i_max = 0; d_max = 0 # d = nums[i] - nums[j]

        for k in range(n):
            res = max(res, d_max * nums[k])
            d_max = max(d_max, x_i_max - nums[k])
            x_i_max = max(x_i_max, nums[k])
        return res