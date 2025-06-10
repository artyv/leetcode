class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        odd_max = 0
        even_min = float('inf')
        for v in counter.values():
            if v % 2 == 0:
                even_min = min(even_min, v)
            else:
                odd_max = max(odd_max, v)
        
        return odd_max - even_min
