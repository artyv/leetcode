class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        unique = set()
        n = len(nums)
        for i in range(n-1, -1, -1):
            if nums[i] not in unique:
                unique.add(nums[i])
            else:
                break
        return math.ceil((n - len(unique)) / 3)