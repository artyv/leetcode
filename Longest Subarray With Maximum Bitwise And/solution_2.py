class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = max(nums)
        lmax = 1; i = 0
        while i < len(nums)-1:
            lc = 1
            if nums[i] == k:
                j = i + 1
                while nums[j] == k and j < len(nums):
                    lc += 1
                    j += 1
                    lmax = max(lmax, lc)
            i += lc
        return lmax
