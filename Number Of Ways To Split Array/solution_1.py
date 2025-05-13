class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        splits = 0
        left = nums[0]
        right = sum(nums[i] for i in range(1, len(nums)))
        if left >= right:
            splits += 1
        
        for i in range(1, len(nums)-1):
            left += nums[i]
            right -= nums[i]
            if left >= right:
                splits += 1
        
        return splits