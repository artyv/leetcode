class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        d = {i:[] for i in range(n)}
        for f, t in edges:
            d[t].append(f)
        print(d)
        for k, v in d.items():
            for el in v:
                if d[el]:
                    d[k].extend(d[el])
            d[k] = sorted(list(set(d[k])))
        return d.values()
        
        
        