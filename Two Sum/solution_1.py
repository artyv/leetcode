class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''for i in range(0, len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        '''
        nums_sorted = sorted([(ind, val) for ind, val in enumerate(nums)], key = lambda x: x[1])

        l = 0; r = len(nums) - 1
        while r != l:
            if nums_sorted[l][1] + nums_sorted[r][1] == target:
                return [nums_sorted[l][0], nums_sorted[r][0]]
            elif nums_sorted[l][1] + nums_sorted[r][1] > target:
                r -= 1
            else:
                l += 1 