class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 1 or k == 0:
            return None
        k = k % len(nums)
        nums_copy = [0] * len(nums)
        for i in range(len(nums)):
            nums_copy[i] = nums[i-k] 
        
        nums[:] = nums_copy
        