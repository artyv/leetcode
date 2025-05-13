class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        n = len(nums)
        d = dict()
        for i in range(n):
            if nums[i] - i in d:
                d[nums[i]-i] += 1
            else:
                d[nums[i]-i] = 1
        
        for k,v in d.items():
            good_pairs += v*(v-1)//2
        
        return n*(n-1)//2 - good_pairs