class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing = decreasing = 1
        istart = dstart = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]: pass
            else:
                increasing = max(increasing,i-istart)
                istart = i
            
            if nums[i] < nums[i-1]: pass
            else:
                decreasing = max(decreasing,i-dstart)
                dstart = i
        increasing = max(increasing,len(nums)-istart)
        decreasing = max(decreasing,len(nums)-dstart)
        return max(increasing,decreasing)
