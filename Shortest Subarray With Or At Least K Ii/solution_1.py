class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if max(nums) >= k:
            return 1
        lmin = 10**10
        len_nums = len(nums)
        l, r = 0, 0
        bit_or = 0
        while r < len_nums:
            while r < len_nums and bit_or | nums[r] < k:
                bit_or |= nums[r]
                r += 1

            lmin = min(lmin, r-l+1)
            while l < r:
                bit_or ^= nums[l]
                l += 1
                if bit_or >= k:
                    lmin = min(lmin, r-l+1)
                else:
                    break
        return lmin if lmin <= len_nums else -1

