class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        splits = 0
        l = len(nums)
        left = 0
        right = sum(nums[i] for i in range(l))
        
        for i in range(l-1):
            left += nums[i]
            right -= nums[i]
            if left >= right:
                splits += 1
        
        return splits