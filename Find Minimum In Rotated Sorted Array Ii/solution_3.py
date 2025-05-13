class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0; right = len(nums) - 1
        nmin = 10**10

        while left <= right:
            i = (left + right) // 2
    
            if nums[left] == nums[i]:
                left += 1
            elif nums[left] < nums[i]:
                nmin = min(nmin, nums[left])
                left = i + 1
            else:
                nmin = min(nmin, nums[i])
                left += 1
                right = i - 1
        return nmin