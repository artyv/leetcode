class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count_W = 0

        for i in range(k):
            if blocks[i] == 'W':
                count_W += 1
        
        min_counter = count_W
        
        for i in range(k, len(blocks)-k+1):
            if blocks[i] == blocks[i-k]:
                continue
            if blocks[i] == 'W':
                count_W += 1
            else:
                count_W -= 1
            min_counter = min(min_counter, count_W)
        
        return min_counter