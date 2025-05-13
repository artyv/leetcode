class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        counter = [0] * n
        for a, b in roads:
            counter[a] += 1
            counter[b] += 1
        
        counter.sort()
        total_importance = 0
        for i, x in enumerate(counter):
            total_importance += (i+1) * x
        
        return total_importance