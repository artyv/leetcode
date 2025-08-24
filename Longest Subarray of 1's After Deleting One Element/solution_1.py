class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count_zeros = 0
        l = 0
        lmax = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                count_zeros += 1
            while count_zeros > 1:
                if nums[l] == 0:
                    count_zeros -= 1
                l += 1
            lmax = max(lmax, r-l)
        
        return lmax
