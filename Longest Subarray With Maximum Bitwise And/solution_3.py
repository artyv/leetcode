class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = max(nums)
        lmax = 1; i = 0
        while i < len(nums)-1:
            lc = 1
            if nums[i] == k:
                j = i
                while nums[j+1] == k:
                    lc += 1
                    j += 1
                    if j == len(nums) - 1:
                        break
            lmax = max(lmax, lc)
            i += lc
        return lmax
