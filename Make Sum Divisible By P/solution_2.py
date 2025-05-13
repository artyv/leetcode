class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remainder = sum(nums) % p
        if remainder == 0:
            return 0

        len_nums = len(nums)
        mapping = {0: -1}
        lmin = 10**10; cur_sum = 0

        for i in range(len_nums):
            cur_sum = (cur_sum + nums[i]) % p
            needed = (cur_sum - remainder + p) % p
            if needed in mapping:
                lmin = min(lmin, i - mapping[needed])
            
            mapping[cur_sum] = i

        return lmin if lmin != len_nums else -1