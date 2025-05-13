class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        l = len(s)
        if k > l:
            return False
        elif k == l:
            return True
        
        d = Counter(s)
        counter = 0
        for key,value in d.items():
            if value % 2 == 1:
                counter += 1
            if counter > k:
                return False
        return True