import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-each for each in gifts]
        heapify(gifts)
        for i in range(k): heapq.heappush(gifts,-floor((-heapq.heappop(gifts))**0.5))
        return -sum(gifts)


        