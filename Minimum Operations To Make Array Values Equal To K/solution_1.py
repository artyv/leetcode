class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if min(nums) < k:
            return -1
        else:
            return len(set([x for x in nums if x > k]))