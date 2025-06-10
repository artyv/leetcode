class Solution:
    def clearStars(self, s: str) -> str:
        pq = [] # (char, -index)
        
        deleted_indices = set()
        
        for i, c in enumerate(s):
            if c == '*':
                if pq:
                    _, neg_index = heapq.heappop(pq)
                    deleted_indices.add(-neg_index)
            else:
                heapq.heappush(pq, (c, -i))
        
        res = []
        for i, c in enumerate(s):
            if c != '*' and i not in deleted_indices:
                res.append(c)
                
        return "".join(res)

