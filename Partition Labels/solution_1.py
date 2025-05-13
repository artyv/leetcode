class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occur = {c:i for i,c in enumerate(s)}

        partitions = []
        n = len(s)
        start, end = 0, 0

        for i, c in enumerate(s):
            end = max(end, last_occur[c])

            if i == end:
                partitions.append(end - start + 1)
                start = i + 1
        
        
        return partitions
            
