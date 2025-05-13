class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.min_weight = [10**10] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y, weight):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
                self.min_weight[root_x] &= self.min_weight[root_y] & weight
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
                self.min_weight[root_y] &= self.min_weight[root_x] & weight
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
                self.min_weight[root_x] &= self.min_weight[root_y] & weight
        else:
            self.min_weight[root_x] &= weight

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        answer = [-1] * len(query)
        dsu = DSU(n)

        for u, v, w in edges:
            root_u = dsu.find(u)
            root_v = dsu.find(v)

            if root_u != root_v:
                dsu.union(u, v, w)
            
            root = dsu.find(u)
            if dsu.min_weight[root] == 0:
                dsu.min_weight[root] = w
            else:
                dsu.min_weight[root] &= w

        for i, (start, end) in enumerate(query):
            if dsu.find(start) == dsu.find(end):
                answer[i] = dsu.min_weight[dsu.find(start)]
            
        return answer