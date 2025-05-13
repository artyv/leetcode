class Solution:
    def specialArray(self, nums: List[int]) -> int:
        if all(el == 0 for el in nums):
            return -1
        nums.sort(reverse=True)
        x = 0
        for n in nums:
            if n >= x:
                x += 1
        return x