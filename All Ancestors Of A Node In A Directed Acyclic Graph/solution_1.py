class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res = [[] for _ in range(n)]
        d = {i:[] for i in range(n)}
        for f, t in edges:
            d[f].append(t)

        def dfs(x, curr):
            for el in d[curr]:
                if res[el] and res[el][-1] == x: 
                    continue
                res[el].append(x)
                dfs(x, el) 

        for i in range(n): 
            dfs(i, i)
        return res
        
        