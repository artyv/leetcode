class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        for c in s:
            if c == '[':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
        return (balance + 1) // 2 # a bit tricky way