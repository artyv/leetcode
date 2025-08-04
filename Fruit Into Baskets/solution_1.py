class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        nmax = 0
        seen = dict()
        for r in range(len(fruits)):
            seen[fruits[r]] = seen.get(fruits[r], 0) + 1 
            while len(seen) > 2:
                seen[fruits[l]] -= 1
                if seen[fruits[l]] == 0:
                    del seen[fruits[l]]
                l += 1
            nmax = max(nmax, r-l+1)
        
        return nmax
