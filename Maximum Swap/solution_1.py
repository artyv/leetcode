class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = []
        while num:
            digits.append(num%10)
            num //= 10
        digits = digits[::-1]
        copy = sorted(digits, reverse=True)
        for i in range(len(digits)):
            if digits[i] != copy[i]:
                ind = digits[i:].index(copy[i])
                digits[i], digits[ind] = digits[ind], digits[i]
                break
        res = digits[0]
        for d in digits[1:]:
            res = res * 10 + d
        return res