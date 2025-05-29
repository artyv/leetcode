class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def build_graph(edges):
            graph = defaultdict(list)
            len_ = 0
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
                len_ = max(len_, u+1, v+1)
            return graph, len_
        
        graph1, n = build_graph(edges1)
        graph2, m = build_graph(edges2)
        
        # will count nodes instead of adding all of them to the list
        def dfs_count(node, parent, graph, depth, depth_max):
            if depth > depth_max:
                return 0
            count = 1
            for cur in graph[node]:
                if cur != parent:
                    count += dfs_count(cur, node, graph, depth+1, depth_max)
            return count

        max_rt2 = 0
        for i in range(m):
            count = dfs_count(i, -1, graph2, 0, k-1)
            max_rt2 = max(max_rt2, count)

        answer = [0] * n
        for i in range(n):
            count = dfs_count(i, -1, graph1, 0, k)
            answer[i] = count + max_rt2

        return answer
