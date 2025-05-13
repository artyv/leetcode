class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        canReachEnd = [l-1]

        for i in range(l-2, -1, -1):
            if nums[i] > 0:
                for j in range(len(canReachEnd)-1, -1, -1):
                    if nums[i] + i >= canReachEnd[j]:
                        canReachEnd.append(i)
                        break
        if canReachEnd[-1] == 0:
            return True
        return False