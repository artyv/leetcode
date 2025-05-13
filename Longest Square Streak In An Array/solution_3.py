class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        squares = set()
        nums = set(nums)
        for x in nums:
            if sqrt(x).is_integer() or x**2 in nums:
                squares.add(x)
        if not squares or len(squares) == 1:
            return -1
        print(squares)
        # [2, 4, 5, 9, 16, 25]
        squares = sorted(list(squares))
        lmax = 1
        checked = set()
        for x in squares:
            if x not in checked:
                checked.add(x)
                lcur = 1
                cur = x
                while cur**2 in squares:
                    lcur += 1
                    lmax = max(lmax, lcur)
                    cur = cur**2
                    checked.add(cur)
        return lmax