class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        res = n * [0.0]
        res[start_node] = 1.0

        pq = [(-1.0, start_node)]
        while pq:
            cur_prob, cur_node = heapq.heappop(pq)
            if cur_node == end_node:
                return -cur_prob
            for nxt_node, path_prob in graph[cur_node]:
                if -cur_prob * path_prob > res[nxt_node]:
                    res[nxt_node] = -cur_prob * path_prob
                    heapq.heappush(pq, (-res[nxt_node], nxt_node))
        return 0.0