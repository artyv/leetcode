class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        more = []
        less = []
        equal = []

        for x in nums:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                more.append(x)
        
        less.extend(equal)
        less.extend(more)
        
        return less