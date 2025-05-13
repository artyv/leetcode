class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = set()
        all_needed = set(range(1, n*n+1))
        twice_seen = -1

        for x in grid:
            for y in x:
                if y in seen:
                    twice_seen = y
                else:
                    seen.add(y)
        
        return [twice_seen, *all_needed.difference(seen)]