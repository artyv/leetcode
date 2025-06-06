class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0; right = len(nums) - 1
        nmin = 10**10

        while left <= right:
            i = (left + right) // 2
    
            if nums[left] <= nums[i]:
                nmin = min(nmin, nums[left])
            else:
                nmin = min(nmin, nums[i])
            left = i + 1
        return nmin