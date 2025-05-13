class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        l = len(nums); max_ramp = 0
        aux = [-1] * l
        aux[-1] = nums[-1]
        for i in range(l-2, -1, -1):
            aux[i] = max(nums[i], aux[i+1])
        
        for i in range(l):
            for j in range(l-1, i, -1):
                if aux[j] >= nums[i]:
                    max_ramp = max(max_ramp, j-i)
                    break
        
        return max_ramp