class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remainder = sum(nums) % p
        if remainder == 0:
            return 0

        len_nums = len(nums)
        prefix_sums_remainder = [sum(nums[:end]) % p for end in range(1, len_nums+1)]
        mapping = {0: -1}
        lmin = 10**10

        for i in range(len_nums):
            needed = (prefix_sums_remainder[i] - remainder + p) % p
            if needed in mapping:
                lmin = min(lmin, i - mapping[needed])
            
            mapping[prefix_sums_remainder[i]] = i

        return lmin if lmin != len_nums else -1