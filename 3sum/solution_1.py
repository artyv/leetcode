class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()
        for i in range(len(nums)-2):
            l = i + 1; r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    output.add((nums[i], nums[l], nums[r]))
                    l += 1; r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                else:
                    r -= 1
        return output