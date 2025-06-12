class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = abs(nums[-1] - nums[0])
        for i in range(len(nums)-1):
            max_diff = max(max_diff, abs(nums[i]-nums[i+1]))
        return max_diff
