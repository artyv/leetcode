class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return None
        output = []
        cur_start = nums[0]
        for i in range(1, len(nums)):
            if abs(nums[i] - nums[i-1]) > 1:
                if cur_start == nums[i-1]:
                    output.append(f"{cur_start}")
                else:
                    output.append(f"{cur_start}->{nums[i-1]}")
                cur_start = nums[i]
        if cur_start == nums[-1]:
            output.append(f"{cur_start}")
        else:
            output.append(f"{cur_start}->{nums[-1]}")
        return output
                