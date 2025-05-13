class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        x = int(s, 2)
        while x != 1:
            x = x // 2 if x % 2 == 0 else x + 1
            steps += 1
        return steps