class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        max_p = max(x, y); min_p = min(x, y)
        if max_p == x:
            more = 'ab'; less = 'ba'
        else:
            more = 'ba'; less = 'ab'
        score = 0
        stack1 = []
        for c in s:
            if stack1 and stack1[-1] + c == more:
                score += max_p
                stack1.pop()
            else:
                stack1.append(c)
        
        stack2 = []
        for c in stack1:
            if stack2 and stack2[-1] + c == less:
                score += min_p
                stack2.pop()
            else:
                stack2.append(c)

        return score

            