class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        aux = sorted(arr)
        ranking = 1
        d = {aux[0]:ranking}
        for i in range(1, len(arr)):
            if aux[i] != aux[i-1]:
                ranking += 1
            d[aux[i]] = ranking
        
        res = []
        for x in arr:
            res.append(d[x])
        return res