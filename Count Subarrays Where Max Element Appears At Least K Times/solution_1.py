class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        xmax = max(nums)
        len_nums = len(nums)
        counter = 0
        l, max_count = 0, 0
        for r in range(len_nums):
            if nums[r] == xmax:
                max_count += 1
            
            while l <= r and max_count >= k:
                counter += len_nums - r
                if nums[l] == xmax:
                    max_count -= 1
                l += 1
        
        return counter
            
