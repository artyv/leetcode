class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        prev1 = 0; prev2 = 0

        for x in nums:
            prev1, prev2 = max(prev2 + x, prev1), prev1
        
        return prev1