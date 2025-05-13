class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[x] for i,x in enumerate(nums)]