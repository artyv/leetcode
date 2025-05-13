class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        def flip(my_list, index):
            for i in range(index, index+k):
                my_list[i] = (my_list[i] + 1) % 2
        
        flips = 0
        for i in range(len(nums)-k+1):
            if nums[i] == 0:
                flip(nums, i)
                flips += 1
        if any(x == 0 for x in nums):
            return -1

        return flips