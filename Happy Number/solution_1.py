class Solution:
    def isHappy(self, n: int) -> bool:
        numbers_seen = set()

        while True:
            n = sum(int(d)**2 for d in str(n))
            if n == 1:
                return True
            if n in numbers_seen:
                return False
            numbers_seen.add(n)