class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        d = dict()
        l, r = 0, 0

        n = len(nums)
        count_pairs = 0
        count_good = 0
        
        for r, x in enumerate(nums):
            d[x] = d.get(x, 0) + 1
            count_pairs += d[x] - 1
            
            while count_pairs >= k:
                count_good += n - r # good subarrays from left to n
                count_pairs -= d[nums[l]] - 1
                d[nums[l]] -= 1
                l += 1

        return count_good