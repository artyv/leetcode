class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        # can fix j and k => two loops only
        x_i_max = nums[0]

        for k in range(2, n):
            for j in range(1, k):
                res = max(res, (x_i_max - nums[j]) * nums[k])
                x_i_max = max(x_i_max, nums[j])
        return res