class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                counter += 1
                nums[i] = 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
        
        return counter if nums[-1] and nums[-2] else -1