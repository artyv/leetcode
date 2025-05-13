class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        missing_sum = 1
        i = 0

        while missing_sum <= n:
            if i < len(nums) and nums[i] <= missing_sum:
                missing_sum += nums[i]
                i += 1
            else:
                missing_sum *= 2 # all old sums + missing_sum are possible now
                patches += 1
        return patches