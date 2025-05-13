class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        indices = []
        for i in range(len(nums)):
            if nums[i] == val:
                indices.append(i)
        for index in indices[::-1]:
            nums.pop(index)
        return len(nums)