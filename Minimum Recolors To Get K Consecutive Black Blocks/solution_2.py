class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_counter = 10**10

        for i in range(len(blocks) - k + 1):
            min_counter = min(min_counter, blocks[i:i+k].count('W'))
        
        return min_counter