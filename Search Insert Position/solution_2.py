class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = bisect.bisect(nums, target)
        return i if target not in nums else i-1