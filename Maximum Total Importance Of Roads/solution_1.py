class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        counter = {}
        for x in roads:
            for i in range(2):
                if x[i] in counter:
                    counter[x[i]] += 1
                else:
                    counter[x[i]] = 1
        counter = sorted(counter.values())
        total_importance = 0
        for i, x in enumerate(counter):
            total_importance += (i+1) * x
        
        return total_importance