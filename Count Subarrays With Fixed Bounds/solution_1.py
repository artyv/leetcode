class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        answer = 0
        last_min = last_max = bad = -1
        
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                bad = i
            if num == minK:
                last_min = i
            if num == maxK:
                last_max = i
            
            valid_start = min(last_min, last_max)
            if valid_start > bad:
                answer += valid_start - bad
        
        return answer