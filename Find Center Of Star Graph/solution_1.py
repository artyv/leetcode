class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a, b = edges[0][0], edges[0][1]
        return a if a in edges[1] else b