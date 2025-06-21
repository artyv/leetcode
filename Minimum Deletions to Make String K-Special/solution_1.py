class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = sorted(Counter(word).values())

        min_dels = float('inf')
        
        for t in set(freq):
            dels = 0
            for f in freq:
                if f < t:
                    dels += f
                elif f > t + k:
                    dels += f - (t + k)
            min_dels = min(min_dels, dels)

        return min_dels
