class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res, maxHeap = "", []
        m = [(-a, "a"), (-b,"b"), (-c,"c")]
        for count, character in m:
            if count:
                heapq.heappush(maxHeap,(count,character))
        while maxHeap:
            count, character = heapq.heappop(maxHeap)

            if len(res) > 1 and res[-1] == res[-2] == character:
                if not maxHeap:
                    break
                c2, char2 = heapq.heappop(maxHeap)
                res+=char2
                c2+=1
                if c2:
                    heapq.heappush(maxHeap,(c2, char2))
            else:
                res+=character
                count+=1
            if count:
                heapq.heappush(maxHeap,(count,character))

        return res
