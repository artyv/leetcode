class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i] and format(nums[j], '0b').count('1') != format(nums[i], '0b').count('1'):
                    return False
        return True