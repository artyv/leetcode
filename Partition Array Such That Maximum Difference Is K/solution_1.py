class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        num_subseq = 1
        cur_min = nums[0]
        for x in nums:
            if x - cur_min > k:
                cur_min = x
                num_subseq += 1
        return num_subseq
