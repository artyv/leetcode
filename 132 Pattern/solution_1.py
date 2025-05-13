class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s = ''
        for i in range(0, len(nums)-1):
            if nums[i+1] > nums[i]:
                s += '+'
            elif nums[i+1] < nums[i]:
                s += '-'
        return '+-' in s 