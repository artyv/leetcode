class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        length = floor(log2(max(start, goal))) + 1
        start_b = format(start, f'0{length}b')
        goal_b = format(goal, f'0{length}b')

        counter = 0
        for i in range(length):
            if start_b[i] != goal_b[i]:
                counter += 1
        return counter
        
