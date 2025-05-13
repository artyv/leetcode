class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l_max = 1
        bitmask = nums[0]
        left = 0

        for right in range(1, len(nums)):
            while (bitmask & nums[right]) != 0:
                bitmask ^= nums[left]
                left += 1
            
            bitmask |= nums[right]
            l_max = max(l_max, right - left + 1)
        
        return l_max

