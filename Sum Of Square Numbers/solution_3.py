class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = [x**2 for x in range(0, int(math.sqrt(c))+1)]
        l = 0; r = len(squares)-1
        while l <= r:
            two_sum = squares[l] + squares[r]
            if two_sum == c:
                return True
            elif two_sum < c:
                l += 1
            else:
                r -= 1
        return False
