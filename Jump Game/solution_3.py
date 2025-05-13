class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        if l == 1:
            return True
        if nums.count(0) == 0:
            return True

        index_max = 0

        for i in range(l-1):
            index_max = max(index_max, i + nums[i])
            if index_max >= l-1:
                return True
            elif index_max == i:
                return False