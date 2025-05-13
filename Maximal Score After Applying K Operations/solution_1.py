class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums.sort()
        score = 0
        for _ in range(k):
            temp = nums.pop()
            score += temp
            nums.insert(bisect.bisect(nums, ceil(temp/3)), ceil(temp/3))
        return score