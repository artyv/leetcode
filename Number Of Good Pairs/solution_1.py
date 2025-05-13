class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0
        if len(nums) == len(set(nums)):
            return counter
        
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    counter += 1

        return counter
