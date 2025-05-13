class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        inc_length = dec_length = max_length = 1
        l_inc, l_dec, l_max = 1, 1, 1

        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                l_inc += 1
                l_dec = 1 
            elif nums[i + 1] < nums[i]:
                l_dec += 1
                l_inc = 1
            else:
                l_inc = 1
                l_dec = 1

            l_max = max(l_max, l_inc, l_dec)

        return l_max