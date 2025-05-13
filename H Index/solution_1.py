class Solution:
    def hIndex(self, citations: List[int]) -> int:
        freq = {c:citations.count(c) for c in set(citations)}
        cur_sum = 0

        for k,v in sorted(freq.items(), reverse=True):
            cur_sum += v
            if cur_sum >= k:
                return k
        
