class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i0 = 0; i1 = nums.count(0); i2 = len(nums)-1; 
        nums_copy = [-1] * len(nums)

        for x in nums:
            if x == 0:
                nums_copy[i0] = 0
                i0 += 1
            elif x == 1:
                nums_copy[i1] = 1
                i1 += 1
            else:
                nums_copy[i2] = 2
                i2 -= 1
        nums[:] = nums_copy