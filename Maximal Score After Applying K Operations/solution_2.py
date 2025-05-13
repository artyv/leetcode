class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums.sort()
        score = 0
        if k < len(nums):
            nums[:] = nums[len(nums)-k-1:]
        print(nums)
        for _ in range(k):
            temp = nums.pop()
            score += temp
            nums.insert(bisect.bisect(nums, ceil(temp/3)), ceil(temp/3))
        return score