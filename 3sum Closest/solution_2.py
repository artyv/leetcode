class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = 10**10
        nums.sort()
        length = len(nums)
        flag = False
        for i in range(length-2):
            if flag:
                break
            if i - 1 >= 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1; r = length - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    closest = target
                    flag = True
                    break
                elif s < target:
                    if abs(s - target) < abs(closest - target):
                        closest = s
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                else:
                    if abs(s - target) < abs(closest - target):
                        closest = s 
                    r -= 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
        
        return closest