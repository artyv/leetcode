class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        canReachEnd = l-1

        for i in range(l-2, -1, -1):
            #if nums[i] > 0:
            if nums[i] + i >= canReachEnd:
                canReachEnd = i
        if canReachEnd == 0:
            return True
        return False