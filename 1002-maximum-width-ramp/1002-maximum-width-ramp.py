class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        mon, length, prev = [], 0, float('inf')

        for i,n in enumerate(nums):
            if n < prev:
                mon.append(i)
                prev = n
        for i in range(len(nums)-1,-1,-1):
            while mon and nums[mon[-1]] <= nums[i]:
                length = max(length,(i-mon[-1]))
                mon.pop()
        return length