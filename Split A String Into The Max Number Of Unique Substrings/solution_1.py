class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        def backtrack(start):
            if start == len(s):
                return 0
            
            counter = 0
            for end in range(start+1, len(s)+1):
                sub_s = s[start:end]
                if sub_s not in seen:
                    seen.add(sub_s)
                    counter = max(counter, 1 + backtrack(end))
                    seen.remove(sub_s)
            return counter
        
        return backtrack(0)