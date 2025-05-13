class Solution:
    def minimumSteps(self, s: str) -> int:
        counter = 0
        min_pos_1 = s.count('0')
        for i in range(len(s)):
            if s[i] == '1':
                counter += min_pos_1 - i
                min_pos_1 += 1
        return counter