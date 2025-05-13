class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sub_sum = 0; left = 0
        kmin = float('inf')
        
        for right in range(len(nums)):
            sub_sum += nums[right]
            while sub_sum >= target:
                kmin = min(kmin, right-left+1)
                sub_sum -= nums[left]
                left += 1
        return kmin if kmin != float('inf') else 0
        