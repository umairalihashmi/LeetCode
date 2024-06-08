class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hash = { 0:-1 }
        presum = 0
        for i in range(len(nums)):
            presum+=nums[i]
            rem = presum%k
            if not rem in hash:
                hash[rem] = i
            elif i - hash[rem] > 1:
                return True
        return False 


        