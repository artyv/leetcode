class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)
        n = 0; m = 0

        for u,v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)
            n = max(n, u+1, v+1)
        
        for u,v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)
            m = max(m, u+1, v+1)
        
        reach_tree1 = [[] for _ in range(n)]
        reach_tree2 = [[] for _ in range(m)]
        

        def dfs(node, parent, graph, depth, depth_max, path):
            if depth > depth_max:
                return
            path.append(node)
            for cur in graph[node]:
                if cur != parent:
                    dfs(cur, node, graph, depth+1, depth_max, path)
        
        for i in range(n):
            path = []
            dfs(i, -1, graph1, 0, k, path)
            reach_tree1[i] = path

        for i in range(m):
            path = []
            dfs(i, -1, graph2, 0, k-1, path)
            reach_tree2[i] = path

        max_rt2 = max(list(map(len, reach_tree2)))
        answer = [0] * n
        for i in range(n):
            answer[i] = len(reach_tree1[i]) + max_rt2

        return answer
