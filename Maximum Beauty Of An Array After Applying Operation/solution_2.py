class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        len_nums = len(nums)
        if nums[-1] - nums[0] <= 2*k:
            return len_nums
        
        lmax = 1
        for i, x in enumerate(nums):
            if len_nums - i < lmax:
                break
            r = x + 2*k
            r_index = bisect.bisect(nums, r)
            lmax = max(lmax, r_index - i)
        return lmax
