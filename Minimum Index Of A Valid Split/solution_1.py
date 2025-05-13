class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dominant = sorted(nums)[len(nums)//2]
        
        freq = dict()
        max_freq = 0; el = -1
        index = -1
        for i, x in enumerate(nums):
            freq[x] = freq.get(x, 0) + 1
            if freq[x] > max_freq:
                max_freq = freq[x]
                el = x
            if el == dominant and max_freq > (i+1) / 2:
                index = i
                break 
                
        counter = nums[index+1:].count(dominant)       
        
        return index if counter > (len(nums) - index - 1) / 2 else -1
