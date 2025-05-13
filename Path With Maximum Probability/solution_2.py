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

        visited = set()

        for x in enumerate(edges):
            if start_node == x[0]:
                break
        else:
            return 0

        cur_node = start_node
        while len(visited) < n:
            for i,x in enumerate(edges):
                if x[0] == cur_node:
                    res[x[1]] = max(res[x[1]], res[x[0]] + log(succProb[i]))
            visited.add(cur_node)
            if len(visited) == n:
                break
            max_el = max([el for el in res if res.index(el) not in visited], default=-1)
            if max_el == -1:
                break
            cur_node = res.index(max_el)
            if cur_node == end_node:
                break
        return e**res[end_node]