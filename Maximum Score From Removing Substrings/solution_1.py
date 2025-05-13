class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        max_p = max(x, y); min_p = min(x, y)
        if max_p == x:
            more = 'ab'; less = 'ba'
        else:
            more = 'ba'; less = 'ab'
        score = 0
        while more in s or less in s:
            if more in s:
                s = s.replace(more, '', 1)
                score += max_p
            else:
                s = s.replace(less, '', 1)
                score += min_p
        return score

            