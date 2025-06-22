class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = [s[i:i+k] for i in range(0, len(s), k)]
        
        len_last = len(res[-1])
        if len_last < k:
            res[-1] += (k-len_last) * fill
        
        return res
