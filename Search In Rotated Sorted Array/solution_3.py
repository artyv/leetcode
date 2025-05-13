class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0; right = len(nums) - 1; i = 0
        k = self.position_index(nums, 0, len(nums) - 1)
        nums_transformed = nums[k:] + nums[:k]
        while left <= right:
            i = (left + right) // 2
            if nums_transformed[i] < target:
                left = i + 1
            elif nums_transformed[i] > target:
                right = i - 1
            else:
                return (k + i) % len(nums)
        return -1

    
    def position_index(self, nums: List[int], left: int, right: int) -> int:
        if left == right:
            return left
        i = left + (right - left) // 2
        
        if nums[i] < nums[i-1]:
            return i 
        elif nums[i] > nums[i+1]:
            return i+1
    
        if nums[left] > nums[i]:
            return position_index(nums, left, i - 1)
        else:
            return position_index(nums, i + 1, right)