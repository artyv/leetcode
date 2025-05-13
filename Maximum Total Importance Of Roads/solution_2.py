class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        counter = {}
        for x in roads:
            for i in range(2):
                if x[i] in counter:
                    counter[x[i]] += 1
                else:
                    counter[x[i]] = 1
        counter = sorted(counter.values(), reverse=True)
        total_importance = 0
        for x in counter:
            total_importance += n * x
            n -= 1
        
        return total_importance