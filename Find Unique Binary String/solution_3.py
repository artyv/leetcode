class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums_int_set = set([int(x, 2) for x in nums])
        n = len(nums[0])

        for x in range(2**n):
            if x not in nums_int_set:
                return format(x, f'0{n}b') 
