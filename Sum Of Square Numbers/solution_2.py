class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0; r = int(math.sqrt(c))
        while l <= r:
            two_sum = l**2 + r**2
            if two_sum == c:
                return True
            elif two_sum < c:
                l += 1
            else:
                r -= 1
        return False
