class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # [1] = 1
        # [1, 2] = 6
        # [1, 2, 3] = 18   [1, 2] * 3 + [3] * 3   score = sum_ * length

        l, counter = 0, 0
        sum_ = 0 # current sum of elements in subarray
        for r, x in enumerate(nums):
            sum_ += x
            while sum_ * (r - l + 1) >= k:
                sum_ -= nums[l]
                l += 1
            counter += (r - l + 1)
        return counter
