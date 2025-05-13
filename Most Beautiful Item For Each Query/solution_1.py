class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])
        items.sort(key=lambda x: x[1], reverse=True)
        
        res = []

        for q in queries:
            for price, beauty in items:
                if q >= price:
                    res.append(beauty)
                    break
            else:
                res.append(0)

        return res