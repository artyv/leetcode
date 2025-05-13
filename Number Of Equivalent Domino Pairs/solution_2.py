class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs = 0
        
        @lru_cache
        def fact(n):
            if n <= 1:
                return 1
            return n*fact(n-1)
        
        
        d = defaultdict(int)
        for dom in dominoes:
            d[tuple(sorted(dom))] += 1

        
        for v in d.values():
            if v > 1:
                pairs += (fact(v) // (2 * fact(v-2)))

        return pairs