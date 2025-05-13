class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        aux = [0] * (len(words) + 1)
        counter = 0
        for i in range(1, len(words) + 1):
            if words[i-1][0] in vowels and words[i-1][-1] in vowels:
                counter += 1
            aux[i] = counter
        
        ans = len(queries) * [-1]
        for i,q in enumerate(queries):
            ans[i] = aux[q[1] + 1] - aux[q[0]]
        
        return ans
