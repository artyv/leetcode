class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        def backtrack(my_str, start, seen):
            if start == len(my_str):
                return 0
            
            counter = 0
            for end in range(start+1, len(my_str)+1):
                sub_s = s[start:end]
                if sub_s not in seen:
                    seen.add(sub_s)
                    counter = max(counter, 1 + backtrack(my_str, end, seen))
                    seen.remove(sub_s)
            return counter
        
        return backtrack(s, 0, seen)