class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.weights = [0xFFFFFFFF] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y, weight):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            self.weights[root_x] &= weight
            return False
        
        if self.size[root_x] > self.size[root_y]:
            self.size[root_x] += self.size[root_y]
            self.parent[root_y] = root_x
            self.weights[root_x] &= self.weights[root_y] & weight
        else:
            self.size[root_y] += self.size[root_x]
            self.parent[root_x] = root_y
            self.weights[root_y] &= self.weights[root_x] & weight
        
        return True

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        answer = [-1] * len(query)
        dsu = DSU(n)

        for u, v, w in edges:
            dsu.union(u, v, w)

        for i, (start, end) in enumerate(query):
            if dsu.find(start) == dsu.find(end):
                answer[i] = dsu.weights[dsu.find(start)]
            
        return answer
