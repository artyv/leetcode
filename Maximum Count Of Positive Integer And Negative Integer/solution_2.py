class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = neg = 0
        for x in nums:
            if x < 0:
                neg += 1
            elif x > 0:
                pos += 1
        
        return max(pos, neg)