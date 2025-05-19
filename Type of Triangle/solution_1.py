class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums
        if a >= b+c or b >= a+c or c >= a+b:
            return 'none'
        
        counter = Counter(nums)
        l = len(counter)
        if l == 1:
            return 'equilateral'
        elif l == 2:
            return 'isosceles'
        else:
            return 'scalene'
