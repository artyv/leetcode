class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target <= max(nums):
            return 1
        elif len(nums) == 1:
            return 0
    
        left = 0; right = 1
        k = 2; sub_sum = nums[left] + nums[right]
        kmin = 10**10; nums_len = len(nums)
        while right <= nums_len - 1 and k > 1:
            if sub_sum >= target or right == nums_len - 1:
                if sub_sum >= target:
                    kmin = min(kmin, k)
                sub_sum -= nums[left]
                k -= 1
                left += 1
            else:
                right += 1
                sub_sum += nums[right]
                k += 1

        return kmin if kmin != 10**10 else 0