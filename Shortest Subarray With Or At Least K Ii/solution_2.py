class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if max(nums) >= k:
            return 1
        lmin = 10**10
        l, r = 0, 0
        bit_or = 0
        while r < len(nums):
            while r < len(nums) and bit_or | nums[r] < k:
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
        return lmin

