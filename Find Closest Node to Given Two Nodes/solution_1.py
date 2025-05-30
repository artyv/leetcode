class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def get_distance(start):
            dist = [-1] * len(edges)
            curr = start
            d = 0
            while curr != -1 and dist[curr] == -1:
                dist[curr] = d
                d += 1
                curr = edges[curr]
            return dist
        
        d1 = get_distance(node1)
        d2 = get_distance(node2)

        dmax = float('inf')
        ans = -1
        for i in range(len(edges)):
            if d1[i] != -1 and d2[i] != -1:
                dmax_cur = max(d1[i], d2[i])
                if dmax_cur < dmax:
                    dmax = dmax_cur
                    ans = i
        
        return ans
