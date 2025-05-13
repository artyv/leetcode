class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] *= -1
        
        heapq.heapify(gifts)

        for _ in range(k):
            el = heapq.heappop(gifts)
            el = int(abs(el)**0.5) *(-1)
            heapq.heappush(gifts, el)
        
        return sum(gifts) * (-1)