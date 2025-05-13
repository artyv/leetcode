class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        d = {i:True for i in range(n)}

        for x,y in edges:
            if d.get(y, 0) != 0:
                del d[y]
        
        return list(d.keys())[0] if len(d) == 1 else -1