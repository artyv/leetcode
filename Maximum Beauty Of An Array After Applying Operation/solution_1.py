class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        len_nums = len(nums)
        l = 0
        for x in nums:
            if x - nums[l] > 2*k:
                l += 1
        return len_nums - l
