class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        if nums.count(0) > 1:
            return [0] * l
        
        answer = [1]*l
        
        for i in range(1, l):
            answer[i] = answer[i-1] * nums[i-1]
        
        accum = 1
        for i in range(l-1, -1, -1):
            answer[i] *= accum
            accum *= nums[i]

        return answer