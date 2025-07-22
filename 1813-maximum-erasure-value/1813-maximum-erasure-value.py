class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxSum = sum(nums)
        uniqSet = set()
        l,r = 0,1
        maxSubSum = SubSum = nums[l]
        uniqSet.add(nums[l])
        while r < len(nums):
            while nums[r] in uniqSet and l < r: 
                uniqSet.remove(nums[l])
                SubSum -= nums[l]
                l += 1
            uniqSet.add(nums[r])
            SubSum += nums[r]
            if SubSum > maxSubSum: maxSubSum = SubSum
            r+=1
        return maxSubSum
                

                 
        