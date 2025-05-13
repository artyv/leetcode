class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x_product = 1
        count_0 = 0
        for x in nums:
            if x != 0:
                x_product *= x
            else:
                count_0 += 1
        
        if count_0 > 1:
            return [0]*len(nums)
    
        for i in range(len(nums)):
            if nums[i] != 0 and count_0 == 1:
                nums[i] = 0
            elif nums[i] != 0:
                nums[i] = x_product//nums[i]
            else:
                nums[i] = x_product
        return nums