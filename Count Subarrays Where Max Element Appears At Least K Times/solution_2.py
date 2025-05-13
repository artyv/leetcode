class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        n = len(nums)
        counter = 0
        left, max_count = 0, 0
        for right in range(n):
            if nums[right] == max_num:
                max_count += 1
            
            while left <= right and max_count >= k:
                counter += n - right
                if nums[left] == max_num:
                    max_count -= 1
                left += 1
        
        return counter
            
