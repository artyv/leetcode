class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0; right = len(nums) - 1

        while left <= right:
            i = (left + right) // 2

            if nums[i] == nums[right] and nums[i] != target:
                return False

            if nums[i] == target:
                return True
            
            if nums[left] == nums[i]:
                left += 1
             
            if nums[i] > nums[left]:
                if nums[left] <= target < nums[i]:
                    right = i - 1
                else:
                    left = i + 1
            else:
                if nums[i] < target <= nums[right]:
                    left = i + 1
                else:
                    right = i - 1
        return False