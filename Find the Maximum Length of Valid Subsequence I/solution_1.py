class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        len_nums = len(nums)
        parity = nums[0] % 2
        
        count_diff = 1
        for i in range(1, len_nums):
            if parity != nums[i] % 2:
                parity = (parity + 1) % 2
                count_diff += 1
        
        count_even = sum(1 for x in nums if x % 2 == 0)
        count_odd = len_nums - count_even

        return max(count_diff, count_even, count_odd)
