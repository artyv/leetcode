class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        counter = 0
        set_banned = set(banned)
        c_sum = 0
        for x in range(1, n+1):
            if x > maxSum:
                return counter
            if x not in set_banned:
                if c_sum + x <= maxSum:
                    c_sum += x
                    counter += 1
                else:
                    return counter
        return counter