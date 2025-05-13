class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for x in set(nums):
            if nums.count(x) > len(nums) // 2:
                return x