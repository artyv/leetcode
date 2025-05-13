from collections import OrderedDict

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = set(); k = 0

        for x in nums:
            if x not in unique:
                unique.add(x)
                nums[k] = x
                k += 1
        return k
