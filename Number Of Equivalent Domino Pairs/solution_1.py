class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs = 0
        
        d = defaultdict(int)
        for dom in dominoes:
            d[tuple(sorted(dom))] += 1

        
        for v in d.values():
            if v > 1:
                pairs += v*(v-1) // 2

        return pairs