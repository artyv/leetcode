class Solution:
    def coloredCells(self, n: int) -> int:
        # 1 - 1
        # 2 - 5
        # 3 - 13
        # 4 - 25
        counter = 1
        fixed_step = current_step = 4

        while n-1:
            counter += current_step
            current_step += fixed_step
            n -= 1

        return counter