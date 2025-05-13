class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n0 = [0] * nums.count(0); n1 = [1] * nums.count(1); n2 = [2] * nums.count(2)
        nums[:] = n0 + n1 + n2