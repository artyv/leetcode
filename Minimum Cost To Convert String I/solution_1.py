class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = 26
        ord_a = ord('a')
        distance = [[float('inf')] * 26 for _ in range(26)]

        for i in range(n):
            distance[i][i] = 0
        
        for i in range(len(original)):
            if cost[i] < distance[ord(original[i])-ord_a][ord(changed[i])-ord_a]:
                distance[ord(original[i])-ord_a][ord(changed[i])-ord_a] = cost[i]
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        
        accum = 0
        for i in range(len(source)):
            if source[i] != target[i]:
                if distance[ord(source[i])-ord_a][ord(target[i])-ord_a] == float('inf'):
                    return -1
                accum += distance[ord(source[i])-ord_a][ord(target[i])-ord_a]
        return accum