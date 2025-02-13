class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0
        while len(nums) > 1:
            first = heapq.heappop(nums)
            if first >= k: return count
            second = heapq.heappop(nums)
            heapq.heappush( nums, (first*2) + second )
            count += 1
        return count
        