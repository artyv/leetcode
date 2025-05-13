class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        freq = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                freq += 1
            else:
                freq = 1
            
            if freq <= 2:
                nums[k] = nums[i]
                k += 1

        return k