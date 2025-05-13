class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = h = len(citations)
        citations.sort()

        for x in citations:
            if x >= h:
                return h
            h -= 1
        return h