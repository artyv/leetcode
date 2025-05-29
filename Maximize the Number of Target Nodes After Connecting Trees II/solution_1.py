class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
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
        
        depth1 = [0] * n
        depth2 = [0] * m

        def dfs_depth(node, parent, graph, depth):
            for cur in graph[node]:
                if cur != parent:
                    depth[cur] = depth[node] + 1
                    dfs_depth(cur, node, graph, depth)
        
        dfs_depth(0, -1, graph1, depth1)
        dfs_depth(0, -1, graph2, depth2)

        even1 = sum(1 for d in depth1 if d % 2 == 0)
        odd1 = n - even1
        even2 = sum(1 for d in depth2 if d % 2 == 0)
        odd2 = m - even2

        answer = [0] * n
        for i in range(n):
            if depth1[i] % 2 == 0:
                s1 = even1 + even2
                s2 = even1 + odd2
            else:
                s1 = odd1 + even2
                s2 = odd1 + odd2
            answer[i] = max(s1, s2)

        return answer
