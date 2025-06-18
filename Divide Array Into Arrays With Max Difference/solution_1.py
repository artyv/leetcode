class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        LEN = 3
        n = len(nums)
        output = []
        for i in range(0, n, LEN):
            if nums[i+2] - nums[i] > k:
                return []
            output.append([nums[i], nums[i+1], nums[i+2]])

        return output
