class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        stack = set()
        for x in nums:
            if x in stack:
                stack.remove(x)
            else:
                stack.add(x)
        
        return not stack