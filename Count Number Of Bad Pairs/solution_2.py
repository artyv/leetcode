class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if j-i == nums[j] - nums[i]:
                    good_pairs += 1
        
        return n*(n-1)//2 - good_pairs