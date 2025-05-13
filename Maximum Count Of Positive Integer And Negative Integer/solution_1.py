class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg_index = bisect.bisect(nums, -1)
        pos_index = bisect.bisect_left(nums, 1)

        return max(len(nums) - pos_index, neg_index)