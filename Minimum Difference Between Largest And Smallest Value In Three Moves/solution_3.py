class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        l = len(nums)
        min_diff = 10**10

        for start in range(4):
            end = start + (l - 4)
            min_diff = min(min_diff, nums[end] - nums[start])

        return min_diff