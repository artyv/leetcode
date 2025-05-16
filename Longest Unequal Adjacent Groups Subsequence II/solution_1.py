class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def get_hamming(s1, s2):
            return sum(x != y for x, y in zip(s1, s2))
        
        def dfs(u, graph, memo):
            if u in memo:
                return memo[u]
            max_path = [u]
            for v in graph[u]:
                path = dfs(v, graph, memo)
                if len(path) + 1 > len(max_path):
                    max_path = [u] + path
            memo[u] = max_path
            return max_path
        
        d_len = defaultdict(list)
        for i, s in enumerate(words):
            d_len[len(s)].append(i)
        
        best_path = []
        for length, indices in d_len.items():
            graph = defaultdict(list)
            for i in range(len(indices)):
                for j in range(i+1, len(indices)):
                    u, v = indices[i], indices[j]
                    if groups[u] != groups[v] and get_hamming(words[u], words[v]) == 1:
                        graph[u].append(v)
        
            memo = {}

            for start in indices:
                path = dfs(start, graph, memo)
                if len(path) > len(best_path):
                    best_path = path

        return [words[i] for i in best_path]
