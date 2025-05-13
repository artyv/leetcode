class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)

        for i in range(l-1, -1, -1):
            if nums[i] > nums[i-1]:
                break
        else:
            nums.reverse()
            return None
    
        for ind in range(l-1, i-1, -1):
            if nums[i-1] < nums[ind]:
                nums[i-1], nums[ind] = nums[ind], nums[i-1]
                break

        nums[i:] = sorted(nums[i:])