class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        LEN = 3
        n_list = len(nums) // LEN
        output = []
        for i in range(n_list):
            if nums[(i+1)*LEN - 1] - nums[i*LEN] <= k:
                output.append(nums[i*LEN:(i+1)*LEN])
            else:
                return []
        return output
