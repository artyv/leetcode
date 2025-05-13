class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # idea is if there are 2 same remainders on the way, the sub-array
        # between then is gonna be divided by k.
        rem_index = {}
        accum_sum = 0
        for i, x in enumerate(nums):
            accum_sum += x
            r = accum_sum % k

            if r in rem_index:
                if i > rem_index[r] + 1:
                    return True # cannot be a sub-array of 1 element
            else:
                rem_index[r] = i
        return False