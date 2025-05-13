class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0

        d = {nums[i]: [j for j in range(len(nums)) if nums[j] == nums[i]] for i in range(len(nums))}

        for key, value in d.items():
            if len(value) > 1:
                counter += len(value) * (len(value) - 1) // 2

        return counter
