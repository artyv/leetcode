class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        types_remained = 0
        used_baskets = set()
        for fruit in fruits:
            for j, basket in enumerate(baskets):
                if fruit <= basket and j not in used_baskets:
                    used_baskets.add(j)
                    break
            else:
                types_remained += 1
        
        return types_remained
