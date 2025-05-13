class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l = len(nums)
        
        for i in range(l-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        res = [0] * l
        j = 0
        for x in nums:
            if x != 0:
                res[j] = x
                j += 1
        
        return res