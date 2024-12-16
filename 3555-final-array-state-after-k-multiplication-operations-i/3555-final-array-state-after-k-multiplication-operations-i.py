import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        res = [0]*len(nums)
        nums = [[nums[i],i] for i in range(len(nums))]
        heapq.heapify(nums)
        for _ in range(k):
            t = heapq.heappop(nums)
            t[0]*=multiplier
            heapq.heappush(nums,t)
        for each in nums:
            res[each[1]] = each[0]
        return res
