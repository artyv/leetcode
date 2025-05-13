class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_unique = list(set(nums))
        l = len(nums_unique)
        if l == 0 or l == 1:
            return l
        if l == 2:
            if abs(nums_unique[0] - nums_unique[1]) == 1:
                return 2
            else:
                return 1

        neighbors = set(); sequences = set()

        for n in nums_unique:
            if n-1 in neighbors:
                sequences.add(n-1)
            if n+1 in neighbors:
                sequences.add(n+1)
            neighbors.add(n-1)
            neighbors.add(n+1)

        lm = 1; lc = 1
        for x in sequences:
            lc = 3
            while x+1 in sequences: 
                lc += 1
                lm = max(lc, lm)
                x += 1
        return lm