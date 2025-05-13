import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or target not in nums:
            return [-1, -1]

        return [bisect.bisect_left(nums, target), bisect.bisect(nums, target)-1]        
